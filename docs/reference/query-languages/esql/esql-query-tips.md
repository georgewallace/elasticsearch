---
applies_to:
  stack: ga
  serverless: ga
navigation_title: "Query tips"
---

# {{esql}} query tips [esql-query-tips]

This page provides practical guidance for writing {{esql}} queries, covering how to structure a query from data source to output, choose the right commands for your goal, and optimize for performance.

## Building a query step by step [esql-query-tips-steps]

### Identify the data source [esql-query-tips-source]

Every {{esql}} query starts with a [`FROM`](/reference/query-languages/esql/commands/from.md) command that specifies which index or data stream to query. Use wildcards to match multiple indices or data streams.

```esql
FROM logs-*
FROM metrics-*
FROM .ds-*
FROM my-index-2024.*
```

### Narrow by time range [esql-query-tips-time]

For time-series data, use a [`WHERE`](/reference/query-languages/esql/commands/where.md) clause on `@timestamp` early in the query to limit the volume of data processed. The [`NOW()`](/reference/query-languages/esql/functions-operators/date-time-functions/now.md) function returns the current time, and you can subtract [time spans](/reference/query-languages/esql/esql-time-spans.md) from it.

| Goal | Filter |
| ---- | ------ |
| Last hour | `@timestamp > NOW() - 1 hour` |
| Last 24 hours | `@timestamp > NOW() - 24 hours` |
| Last 7 days | `@timestamp > NOW() - 7 days` |
| Yesterday | `@timestamp >= NOW() - 48 hours AND @timestamp < NOW() - 24 hours` |
| Last 30 days | `@timestamp > NOW() - 30 days` |

If no time range is required, consider adding a reasonable default such as the last 24 hours to avoid scanning unnecessarily large amounts of data.

### Add filters [esql-query-tips-filters]

Use additional [`WHERE`](/reference/query-languages/esql/commands/where.md) clauses to narrow results by field values. Multiple conditions can be combined in a single clause or expressed as separate clauses:

```esql
FROM logs-*
| WHERE @timestamp > NOW() - 1 hour
| WHERE log.level == "error" AND environment == "production" AND service.name == "api-gateway"
```

### Choose the right output type [esql-query-tips-output]

The shape of your query depends on whether you want to retrieve raw documents or compute aggregated results.

**Retrieve raw documents** using [`KEEP`](/reference/query-languages/esql/commands/keep.md), [`SORT`](/reference/query-languages/esql/commands/sort.md), and [`LIMIT`](/reference/query-languages/esql/commands/limit.md) when you want to inspect individual events:

```esql
FROM logs-*
| WHERE @timestamp > NOW() - 1 hour
| WHERE log.level == "error"
| KEEP @timestamp, service.name, http.response.status_code, url.path
| SORT @timestamp DESC
| LIMIT 50
```

**Count documents** using [`STATS`](/reference/query-languages/esql/commands/stats-by.md) with [`COUNT`](/reference/query-languages/esql/functions-operators/aggregation-functions/count.md) when you want to know how many events match a condition:

```esql
FROM logs-*
| WHERE @timestamp > NOW() - 1 hour
| WHERE http.response.status_code >= 500
| STATS error_count = COUNT(*)
```

**Compute metrics** using `STATS` with aggregation functions such as [`AVG`](/reference/query-languages/esql/functions-operators/aggregation-functions/avg.md), [`SUM`](/reference/query-languages/esql/functions-operators/aggregation-functions/sum.md), or [`MAX`](/reference/query-languages/esql/functions-operators/aggregation-functions/max.md):

```esql
FROM metrics-*
| WHERE @timestamp > NOW() - 15 minutes
| STATS
    avg_latency = AVG(transaction.duration.us),
    max_latency = MAX(transaction.duration.us)
```

**Group results** by adding a `BY` clause to `STATS`, which partitions the output by distinct field values:

```esql
FROM logs-*
| WHERE @timestamp > NOW() - 1 hour
| STATS request_count = COUNT(*) BY http.response.status_code
| SORT request_count DESC
```

**Find the most frequent values** by combining `STATS` with `SORT ... DESC` and `LIMIT`:

```esql
FROM logs-*
| WHERE @timestamp > NOW() - 24 hours
| STATS request_count = COUNT(*) BY url.path
| SORT request_count DESC
| LIMIT 10
```

**Analyze trends over time** using [`DATE_TRUNC`](/reference/query-languages/esql/functions-operators/date-time-functions/date_trunc.md) in a `STATS ... BY` expression to bucket documents into fixed time intervals:

```esql
FROM logs-*
| WHERE @timestamp > NOW() - 24 hours
| STATS request_count = COUNT(*) BY bucket = DATE_TRUNC(1 hour, @timestamp)
| SORT bucket ASC
```

### Select fields [esql-query-tips-fields]

For raw data queries, use `KEEP` to return only the fields you need:

```esql
| KEEP @timestamp, host.name, message, log.level
```

For aggregation queries, the output columns are defined by the `STATS` expression itself:

```esql
| STATS count = COUNT(*), avg_time = AVG(response_time) BY endpoint
```

### Sort and limit results [esql-query-tips-sort-limit]

Use [`SORT`](/reference/query-languages/esql/commands/sort.md) to control result ordering and [`LIMIT`](/reference/query-languages/esql/commands/limit.md) to cap the number of rows returned. Always include a `LIMIT` for raw data queries.

```esql
| SORT @timestamp DESC
| LIMIT 100
```

---

## Field naming conventions [esql-query-tips-fields-naming]

{{esql}} works with the field names stored in your index. The following table lists common fields from the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current/index.html), which is used by many Elastic integrations and data streams.

| Category | Common fields |
| -------- | ------------- |
| Timestamp | `@timestamp` |
| Message | `message` |
| Log level | `log.level` |
| Host | `host.name`, `host.ip` |
| Service | `service.name`, `service.type` |
| HTTP | `http.request.method`, `http.response.status_code`, `url.path` |
| User | `user.name`, `user.id` |
| Source | `source.ip`, `source.port` |
| Destination | `destination.ip`, `destination.port` |
| Error | `error.message`, `error.type` |
| Event | `event.action`, `event.category`, `event.outcome` |

Custom or legacy indices may use non-ECS field names such as `status_code` instead of `http.response.status_code`, or `hostname` instead of `host.name`. Use the [index mapping APIs](/reference/elasticsearch/rest-apis/index.md) to discover the field names available in a specific index.

---

## Performance tips [esql-query-tips-performance]

### Filter early [esql-query-tips-filter-early]

Place `WHERE` clauses as early as possible in the pipeline, before `STATS` or other processing commands. This reduces the number of rows that subsequent commands must process.

```esql
FROM logs-*
| WHERE @timestamp > NOW() - 1 hour
| WHERE log.level == "error"
| STATS count = COUNT(*) BY host.name
```

Avoid filtering after an aggregation when the filter could have been applied to the source data:

```esql
FROM logs-*
| STATS count = COUNT(*) BY host.name, log.level
| WHERE log.level == "error"
```

### Use a time range [esql-query-tips-time-range]

Always specify a time range on `@timestamp` when querying time-series data. Omitting a time filter causes the query to scan all data in the index.

### Keep only the fields you need [esql-query-tips-keep-fields]

Use `KEEP` to limit the fields returned in raw data queries. Retrieving fewer fields reduces memory usage and network transfer.

```esql
| KEEP @timestamp, message, host.name
```

### Always include LIMIT [esql-query-tips-limit]

For raw data queries, include a `LIMIT` to prevent returning an unexpectedly large result set. The default maximum is 1,000 rows; see [Result set size limit](/reference/query-languages/esql/limitations.md#esql-max-rows).

```esql
| LIMIT 100
```

---

## Example queries [esql-query-tips-examples]

### Error investigation [esql-query-tips-example-errors]

Retrieve the most recent error log entries across all services:

```esql
FROM logs-*
| WHERE @timestamp > NOW() - 1 hour
| WHERE log.level == "error"
| KEEP @timestamp, message, host.name, service.name, error.message
| SORT @timestamp DESC
| LIMIT 100
```

### Service health overview [esql-query-tips-example-health]

Compute average CPU and memory usage per service over the last 15 minutes:

```esql
FROM metrics-*
| WHERE @timestamp > NOW() - 15 minutes
| STATS
    avg_cpu = AVG(system.cpu.percent),
    avg_mem = AVG(system.memory.used.pct),
    host_count = COUNT_DISTINCT(host.name)
  BY service.name
| SORT avg_cpu DESC
```

### API performance analysis [esql-query-tips-example-apm]

Summarize request counts, average duration, and 95th percentile latency per endpoint:

```esql
FROM apm-*
| WHERE @timestamp > NOW() - 1 hour
| STATS
    count = COUNT(*),
    avg_duration = AVG(transaction.duration.us),
    p95_duration = PERCENTILE(transaction.duration.us, 95),
    error_count = COUNT(CASE(transaction.result != "success", 1, null))
  BY transaction.name
| EVAL error_rate = ROUND(error_count * 100.0 / count, 2)
| SORT count DESC
| LIMIT 20
```

### Traffic over time [esql-query-tips-example-traffic]

Count requests and unique client IPs per hour over the last 24 hours:

```esql
FROM web-logs
| WHERE @timestamp > NOW() - 24 hours
| STATS
    requests = COUNT(*),
    unique_ips = COUNT_DISTINCT(client.ip)
  BY bucket = DATE_TRUNC(1 hour, @timestamp)
| SORT bucket DESC
```

### Failed authentication events [esql-query-tips-example-security]

Find users and source IPs with more than five authentication failures in the last 24 hours:

```esql
FROM security-*
| WHERE @timestamp > NOW() - 24 hours
| WHERE event.category == "authentication"
| WHERE event.outcome == "failure"
| STATS failures = COUNT(*) BY user.name, source.ip
| WHERE failures > 5
| SORT failures DESC
```
