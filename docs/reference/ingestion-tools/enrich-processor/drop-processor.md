---
navigation_title: "Drop"
---

# Drop processor [drop-processor]


Drops the document without raising any errors. This is useful to prevent the document from getting indexed based on some condition.

$$$drop-options$$$

| Name | Required | Default | Description |
| --- | --- | --- | --- |
| `description` | no | - | Description of the processor. Useful for describing the purpose of the processor or its configuration. |
| `if` | no | - | Conditionally execute the processor. See [Conditionally run a processor](ingest.md#conditionally-run-processor). |
| `ignore_failure` | no | `false` | Ignore failures for the processor. See [Handling pipeline failures](ingest.md#handling-pipeline-failures). |
| `on_failure` | no | - | Handle failures for the processor. See [Handling pipeline failures](ingest.md#handling-pipeline-failures). |
| `tag` | no | - | Identifier for the processor. Useful for debugging and metrics. |

```js
{
  "drop": {
    "if" : "ctx.network_name == 'Guest'"
  }
}
```

%  NOTCONSOLE

