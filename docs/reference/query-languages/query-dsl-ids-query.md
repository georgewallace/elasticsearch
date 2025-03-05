---
navigation_title: "IDs"
---

# IDs [query-dsl-ids-query]


Returns documents based on their IDs. This query uses document IDs stored in the [`_id`](mapping-id-field.md) field.

## Example request [_example_request_3]

```console
GET /_search
{
  "query": {
    "ids" : {
      "values" : ["1", "4", "100"]
    }
  }
}
```


## Top-level parameters for `ids` [ids-query-top-level-parameters]

`values`
:   (Required, array of strings) An array of [document IDs](mapping-id-field.md).


