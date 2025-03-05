---
navigation_title: "Terminate"
---

# Terminate processor [terminate-processor]


Terminates the current ingest pipeline, causing no further processors to be run. This will normally be executed conditionally, using the `if` option.

If this pipeline is being called from another pipeline, the calling pipeline is **not** terminated.

$$$terminate-options$$$

| Name | Required | Default | Description |
| --- | --- | --- | --- |
| `description` | no | - | Description of the processor. Useful for describing the purpose of the processor or its configuration. |
| `if` | no | - | Conditionally execute the processor. See [Conditionally run a processor](ingest.md#conditionally-run-processor). |
| `ignore_failure` | no | `false` | Ignore failures for the processor. See [Handling pipeline failures](ingest.md#handling-pipeline-failures). |
| `on_failure` | no | - | Handle failures for the processor. See [Handling pipeline failures](ingest.md#handling-pipeline-failures). |
| `tag` | no | - | Identifier for the processor. Useful for debugging and metrics. |

```js
{
  "description" : "terminates the current pipeline if the error field is present",
  "terminate": {
    "if": "ctx.error != null"
  }
}
```

%  NOTCONSOLE

