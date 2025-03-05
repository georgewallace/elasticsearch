---
navigation_title: "Predicate script"
---

# Predicate script token filter [analysis-predicatefilter-tokenfilter]


Removes tokens that don’t match a provided predicate script. The filter supports inline [Painless](https://www.elastic.co/guide/en/elasticsearch/painless/current/index.html) scripts only. Scripts are evaluated in the [analysis predicate context](https://www.elastic.co/guide/en/elasticsearch/painless/current/painless-analysis-predicate-context.html).

## Example [analysis-predicatefilter-tokenfilter-analyze-ex]

The following [analyze API](indices-analyze.md) request uses the `predicate_token_filter` filter to only output tokens longer than three characters from `the fox jumps the lazy dog`.

```console
GET /_analyze
{
  "tokenizer": "whitespace",
  "filter": [
    {
      "type": "predicate_token_filter",
      "script": {
        "source": """
          token.term.length() > 3
        """
      }
    }
  ],
  "text": "the fox jumps the lazy dog"
}
```

The filter produces the following tokens.

```text
[ jumps, lazy ]
```

The API response contains the position and offsets of each output token. Note the `predicate_token_filter` filter does not change the tokens' original positions or offsets.

::::{dropdown} **Response**
```console-result
{
  "tokens" : [
    {
      "token" : "jumps",
      "start_offset" : 8,
      "end_offset" : 13,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "lazy",
      "start_offset" : 18,
      "end_offset" : 22,
      "type" : "word",
      "position" : 4
    }
  ]
}
```

::::



## Configurable parameters [analysis-predicatefilter-tokenfilter-configure-parms]

`script`
:   (Required, [script object](modules-scripting-using.md)) Script containing a condition used to filter incoming tokens. Only tokens that match this script are included in the output.

    This parameter supports inline [Painless](https://www.elastic.co/guide/en/elasticsearch/painless/current/index.html) scripts only. The script is evaluated in the [analysis predicate context](https://www.elastic.co/guide/en/elasticsearch/painless/current/painless-analysis-predicate-context.html).



## Customize and add to an analyzer [analysis-predicatefilter-tokenfilter-customize]

To customize the `predicate_token_filter` filter, duplicate it to create the basis for a new custom token filter. You can modify the filter using its configurable parameters.

The following [create index API](indices-create-index.md) request configures a new [custom analyzer](analysis-custom-analyzer.md) using a custom `predicate_token_filter` filter, `my_script_filter`.

The `my_script_filter` filter removes tokens with of any type other than `ALPHANUM`.

```console
PUT /my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "standard",
          "filter": [
            "my_script_filter"
          ]
        }
      },
      "filter": {
        "my_script_filter": {
          "type": "predicate_token_filter",
          "script": {
            "source": """
              token.type.contains("ALPHANUM")
            """
          }
        }
      }
    }
  }
}
```


