---
navigation_title: "Snowball"
---

# Snowball token filter [analysis-snowball-tokenfilter]


A filter that stems words using a Snowball-generated stemmer. The `language` parameter controls the stemmer with the following available values: `Arabic`, `Armenian`, `Basque`, `Catalan`, `Danish`, `Dutch`, `English`, `Estonian`, `Finnish`, `French`, `German`, `German2`, `Hungarian`, `Italian`, `Irish`, `Kp`, `Lithuanian`, `Lovins`, `Norwegian`, `Porter`, `Portuguese`, `Romanian`, `Russian`, `Serbian`, `Spanish`, `Swedish`, `Turkish`.

[8.16.0]

For example:

```console
PUT /my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "standard",
          "filter": [ "lowercase", "my_snow" ]
        }
      },
      "filter": {
        "my_snow": {
          "type": "snowball",
          "language": "English"
        }
      }
    }
  }
}
```

