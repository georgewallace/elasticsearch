---
navigation_title: "Delimited payload"
---

# Delimited payload token filter [analysis-delimited-payload-tokenfilter]


::::{warning} 
The older name `delimited_payload_filter` is deprecated and should not be used with new indices. Use `delimited_payload` instead.

::::


Separates a token stream into tokens and payloads based on a specified delimiter.

For example, you can use the `delimited_payload` filter with a `|` delimiter to split `the|1 quick|2 fox|3` into the tokens `the`, `quick`, and `fox` with respective payloads of `1`, `2`, and `3`.

This filter uses Lucene’s [DelimitedPayloadTokenFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/payloads/DelimitedPayloadTokenFilter.md).

::::{admonition} Payloads
:class: note

A payload is user-defined binary data associated with a token position and stored as base64-encoded bytes.

{{es}} does not store token payloads by default. To store payloads, you must:

* Set the [`term_vector`](term-vector.md) mapping parameter to `with_positions_payloads` or `with_positions_offsets_payloads` for any field storing payloads.
* Use an index analyzer that includes the `delimited_payload` filter

You can view stored payloads using the [term vectors API](docs-termvectors.md).

::::


## Example [analysis-delimited-payload-tokenfilter-analyze-ex]

The following [analyze API](indices-analyze.md) request uses the `delimited_payload` filter with the default `|` delimiter to split `the|0 brown|10 fox|5 is|0 quick|10` into tokens and payloads.

```console
GET _analyze
{
  "tokenizer": "whitespace",
  "filter": ["delimited_payload"],
  "text": "the|0 brown|10 fox|5 is|0 quick|10"
}
```

The filter produces the following tokens:

```text
[ the, brown, fox, is, quick ]
```

Note that the analyze API does not return stored payloads. For an example that includes returned payloads, see [Return stored payloads](analysis-delimited-payload-tokenfilter.md#analysis-delimited-payload-tokenfilter-return-stored-payloads).

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens": [
%     {
%       "token": "the",
%       "start_offset": 0,
%       "end_offset": 5,
%       "type": "word",
%       "position": 0
%     },
%     {
%       "token": "brown",
%       "start_offset": 6,
%       "end_offset": 14,
%       "type": "word",
%       "position": 1
%     },
%     {
%       "token": "fox",
%       "start_offset": 15,
%       "end_offset": 20,
%       "type": "word",
%       "position": 2
%     },
%     {
%       "token": "is",
%       "start_offset": 21,
%       "end_offset": 25,
%       "type": "word",
%       "position": 3
%     },
%     {
%       "token": "quick",
%       "start_offset": 26,
%       "end_offset": 34,
%       "type": "word",
%       "position": 4
%     }
%   ]
% }
% --------------------------------------------------


## Add to an analyzer [analysis-delimited-payload-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the `delimited-payload` filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

```console
PUT delimited_payload
{
  "settings": {
    "analysis": {
      "analyzer": {
        "whitespace_delimited_payload": {
          "tokenizer": "whitespace",
          "filter": [ "delimited_payload" ]
        }
      }
    }
  }
}
```


## Configurable parameters [analysis-delimited-payload-tokenfilter-configure-parms]

`delimiter`
:   (Optional, string) Character used to separate tokens from payloads. Defaults to `|`.

`encoding`
:   (Optional, string) Data type for the stored payload. Valid values are:

`float`
:   (Default) Float

`identity`
:   Characters

`int`
:   Integer



## Customize and add to an analyzer [analysis-delimited-payload-tokenfilter-customize]

To customize the `delimited_payload` filter, duplicate it to create the basis for a new custom token filter. You can modify the filter using its configurable parameters.

For example, the following [create index API](indices-create-index.md) request uses a custom `delimited_payload` filter to configure a new [custom analyzer](analysis-custom-analyzer.md). The custom `delimited_payload` filter uses the `+` delimiter to separate tokens from payloads. Payloads are encoded as integers.

```console
PUT delimited_payload_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "whitespace_plus_delimited": {
          "tokenizer": "whitespace",
          "filter": [ "plus_delimited" ]
        }
      },
      "filter": {
        "plus_delimited": {
          "type": "delimited_payload",
          "delimiter": "+",
          "encoding": "int"
        }
      }
    }
  }
}
```


## Return stored payloads [analysis-delimited-payload-tokenfilter-return-stored-payloads]

Use the [create index API](indices-create-index.md) to create an index that:

* Includes a field that stores term vectors with payloads.
* Uses a [custom index analyzer](analysis-custom-analyzer.md) with the `delimited_payload` filter.

```console
PUT text_payloads
{
  "mappings": {
    "properties": {
      "text": {
        "type": "text",
        "term_vector": "with_positions_payloads",
        "analyzer": "payload_delimiter"
      }
    }
  },
  "settings": {
    "analysis": {
      "analyzer": {
        "payload_delimiter": {
          "tokenizer": "whitespace",
          "filter": [ "delimited_payload" ]
        }
      }
    }
  }
}
```

Add a document containing payloads to the index.

```console
POST text_payloads/_doc/1
{
  "text": "the|0 brown|3 fox|4 is|0 quick|10"
}
```

%  TEST[continued]

Use the [term vectors API](docs-termvectors.md) to return the document’s tokens and base64-encoded payloads.

```console
GET text_payloads/_termvectors/1
{
  "fields": [ "text" ],
  "payloads": true
}
```

%  TEST[continued]

The API returns the following response:

```console-result
{
  "_index": "text_payloads",
  "_id": "1",
  "_version": 1,
  "found": true,
  "took": 8,
  "term_vectors": {
    "text": {
      "field_statistics": {
        "sum_doc_freq": 5,
        "doc_count": 1,
        "sum_ttf": 5
      },
      "terms": {
        "brown": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 1,
              "payload": "QEAAAA=="
            }
          ]
        },
        "fox": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 2,
              "payload": "QIAAAA=="
            }
          ]
        },
        "is": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 3,
              "payload": "AAAAAA=="
            }
          ]
        },
        "quick": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 4,
              "payload": "QSAAAA=="
            }
          ]
        },
        "the": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 0,
              "payload": "AAAAAA=="
            }
          ]
        }
      }
    }
  }
}
```

%  TESTRESPONSE[s/"took": 8/"took": "$body.took"/]


