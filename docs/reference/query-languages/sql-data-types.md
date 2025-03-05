# Data Types [sql-data-types]

|     |     |     |     |
| --- | --- | --- | --- |
| **{{es}} type** | **Elasticsearch SQL type** | **SQL type** | **SQL precision** |
| Core types |
| [`null`](null-value.md) | `null` | NULL | 0 |
| [`boolean`](boolean.md) | `boolean` | BOOLEAN | 1 |
| [`byte`](number.md) | `byte` | TINYINT | 3 |
| [`short`](number.md) | `short` | SMALLINT | 5 |
| [`integer`](number.md) | `integer` | INTEGER | 10 |
| [`long`](number.md) | `long` | BIGINT | 19 |
| [`unsigned_long`](number.md) | `[preview] unsigned_long` | BIGINT | 20 |
| [`double`](number.md) | `double` | DOUBLE | 15 |
| [`float`](number.md) | `float` | REAL | 7 |
| [`half_float`](number.md) | `half_float` | FLOAT | 3 |
| [`scaled_float`](number.md) | `scaled_float` | DOUBLE | 15 |
| [keyword type family](keyword.md) | `keyword` | VARCHAR | 32,766 |
| [`text`](text.md) | `text` | VARCHAR | 2,147,483,647 |
| [`binary`](binary.md) | `binary` | VARBINARY | 2,147,483,647 |
| [`date`](date.md) | `datetime` | TIMESTAMP | 29 |
| [`ip`](ip.md) | `ip` | VARCHAR | 39 |
| [`version`](version.md) | `version` | VARCHAR | 32,766 |
| Complex types |
| [`object`](object.md) | `object` | STRUCT | 0 |
| [`nested`](nested.md) | `nested` | STRUCT | 0 |
| Unsupported types |
| *types not mentioned above* | `unsupported` | OTHER | 0 |

::::{note} 
Most of {{es}} [data types](mapping-types.md) are available in Elasticsearch SQL, as indicated above. As one can see, all of {{es}} [data types](mapping-types.md) are mapped to the data type with the same name in Elasticsearch SQL, with the exception of ***date*** data type which is mapped to ***datetime*** in Elasticsearch SQL. This is to avoid confusion with the ANSI SQL types ***DATE*** (date only) and ***TIME*** (time only), which are also supported by Elasticsearch SQL in queries (with the use of [`CAST`](sql-functions-type-conversion.md#sql-functions-type-conversion-cast)/[`CONVERT`](sql-functions-type-conversion.md#sql-functions-type-conversion-convert)), but don’t correspond to an actual mapping in {{es}} (see the [`table`](sql-data-types.md#es-sql-only-types) below).
::::


Obviously, not all types in {{es}} have an equivalent in SQL and vice-versa hence why, Elasticsearch SQL uses the data type *particularities* of the former over the latter as ultimately {{es}} is the backing store.

In addition to the types above, Elasticsearch SQL also supports at *runtime* SQL-specific types that do not have an equivalent in {{es}}. Such types cannot be loaded from {{es}} (as it does not know about them) however can be used inside Elasticsearch SQL in queries or their results.

$$$es-sql-only-types$$$
The table below indicates these types:

|     |     |
| --- | --- |
| **SQL type** | **SQL precision** |
| `date` | 29 |
| `time` | 18 |
| `interval_year` | 7 |
| `interval_month` | 7 |
| `interval_day` | 23 |
| `interval_hour` | 23 |
| `interval_minute` | 23 |
| `interval_second` | 23 |
| `interval_year_to_month` | 7 |
| `interval_day_to_hour` | 23 |
| `interval_day_to_minute` | 23 |
| `interval_day_to_second` | 23 |
| `interval_hour_to_minute` | 23 |
| `interval_hour_to_second` | 23 |
| `interval_minute_to_second` | 23 |
| `geo_point` | 52 |
| `geo_shape` | 2,147,483,647 |
| `shape` | 2,147,483,647 |


## SQL and multi-fields [sql-multi-field] 

A core concept in {{es}} is that of an `analyzed` field, that is a full-text value that is interpreted in order to be effectively indexed. These fields are of type [`text`](text.md) and are not used for sorting or aggregations as their actual value depends on the [`analyzer`](analyzer.md) used hence why {{es}} also offers the [`keyword`](keyword.md) type for storing the *exact* value.

In most case, and the default actually, is to use both types for strings which {{es}} supports through [multi-fields](multi-fields.md), that is the ability to index the same string in multiple ways; for example index it both as `text` for search but also as `keyword` for sorting and aggregations.

As SQL requires exact values, when encountering a `text` field Elasticsearch SQL will search for an exact multi-field that it can use for comparisons, sorting and aggregations. To do that, it will search for the first `keyword` that it can find that is *not* normalized and use that as the original field *exact* value.

Consider the following `string` mapping:

```js
{
  "first_name": {
    "type": "text",
    "fields": {
      "raw": {
        "type": "keyword"
      }
    }
  }
}
```

%  NOTCONSOLE

The following SQL query:

```sql
SELECT first_name FROM index WHERE first_name = 'John'
```

is identical to:

```sql
SELECT first_name FROM index WHERE first_name.raw = 'John'
```

as Elasticsearch SQL automatically *picks* up the `raw` multi-field from `raw` for exact matching.

