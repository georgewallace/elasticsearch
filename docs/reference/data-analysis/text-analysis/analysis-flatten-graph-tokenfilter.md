---
navigation_title: "Flatten graph"
---

# Flatten graph token filter [analysis-flatten-graph-tokenfilter]


Flattens a [token graph](token-graphs.md) produced by a graph token filter, such as [`synonym_graph`](analysis-synonym-graph-tokenfilter.md) or [`word_delimiter_graph`](analysis-word-delimiter-graph-tokenfilter.md).

Flattening a token graph containing [multi-position tokens](token-graphs.md#token-graphs-multi-position-tokens) makes the graph suitable for [indexing](analysis-index-search-time.md). Otherwise, indexing does not support token graphs containing multi-position tokens.

::::{warning} 
Flattening graphs is a lossy process.

If possible, avoid using the `flatten_graph` filter. Instead, use graph token filters in [search analyzers](analysis-index-search-time.md) only. This eliminates the need for the `flatten_graph` filter.

::::


The `flatten_graph` filter uses Lucene’s [FlattenGraphFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/core/FlattenGraphFilter.md).

## Example [analysis-flatten-graph-tokenfilter-analyze-ex]

To see how the `flatten_graph` filter works, you first need to produce a token graph containing multi-position tokens.

The following [analyze API](indices-analyze.md) request uses the `synonym_graph` filter to add `dns` as a multi-position synonym for `domain name system` in the text `domain name system is fragile`:

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "synonym_graph",
      "synonyms": [ "dns, domain name system" ]
    }
  ],
  "text": "domain name system is fragile"
}
```

The filter produces the following token graph with `dns` as a multi-position token.

:::{image} images/token-graph-dns-synonym-ex.svg
:alt: token graph dns synonym ex
:::

% [source,console-result]
% ----
% {
%   "tokens": [
%     {
%       "token": "dns",
%       "start_offset": 0,
%       "end_offset": 18,
%       "type": "SYNONYM",
%       "position": 0,
%       "positionLength": 3
%     },
%     {
%       "token": "domain",
%       "start_offset": 0,
%       "end_offset": 6,
%       "type": "<ALPHANUM>",
%       "position": 0
%     },
%     {
%       "token": "name",
%       "start_offset": 7,
%       "end_offset": 11,
%       "type": "<ALPHANUM>",
%       "position": 1
%     },
%     {
%       "token": "system",
%       "start_offset": 12,
%       "end_offset": 18,
%       "type": "<ALPHANUM>",
%       "position": 2
%     },
%     {
%       "token": "is",
%       "start_offset": 19,
%       "end_offset": 21,
%       "type": "<ALPHANUM>",
%       "position": 3
%     },
%     {
%       "token": "fragile",
%       "start_offset": 22,
%       "end_offset": 29,
%       "type": "<ALPHANUM>",
%       "position": 4
%     }
%   ]
% }
% ----

Indexing does not support token graphs containing multi-position tokens. To make this token graph suitable for indexing, it needs to be flattened.

To flatten the token graph, add the `flatten_graph` filter after the `synonym_graph` filter in the previous analyze API request.

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "synonym_graph",
      "synonyms": [ "dns, domain name system" ]
    },
    "flatten_graph"
  ],
  "text": "domain name system is fragile"
}
```

The filter produces the following flattened token graph, which is suitable for indexing.

:::{image} images/token-graph-dns-invalid-ex.svg
:alt: token graph dns invalid ex
:::

% [source,console-result]
% ----
% {
%   "tokens": [
%     {
%       "token": "dns",
%       "start_offset": 0,
%       "end_offset": 18,
%       "type": "SYNONYM",
%       "position": 0,
%       "positionLength": 3
%     },
%     {
%       "token": "domain",
%       "start_offset": 0,
%       "end_offset": 6,
%       "type": "<ALPHANUM>",
%       "position": 0
%     },
%     {
%       "token": "name",
%       "start_offset": 7,
%       "end_offset": 11,
%       "type": "<ALPHANUM>",
%       "position": 1
%     },
%     {
%       "token": "system",
%       "start_offset": 12,
%       "end_offset": 18,
%       "type": "<ALPHANUM>",
%       "position": 2
%     },
%     {
%       "token": "is",
%       "start_offset": 19,
%       "end_offset": 21,
%       "type": "<ALPHANUM>",
%       "position": 3
%     },
%     {
%       "token": "fragile",
%       "start_offset": 22,
%       "end_offset": 29,
%       "type": "<ALPHANUM>",
%       "position": 4
%     }
%   ]
% }
% ----


## Add to an analyzer [analysis-keyword-marker-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the `flatten_graph` token filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

In this analyzer, a custom `word_delimiter_graph` filter produces token graphs containing catenated, multi-position tokens. The `flatten_graph` filter flattens these token graphs, making them suitable for indexing.

```console
PUT /my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_index_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "my_custom_word_delimiter_graph_filter",
            "flatten_graph"
          ]
        }
      },
      "filter": {
        "my_custom_word_delimiter_graph_filter": {
          "type": "word_delimiter_graph",
          "catenate_all": true
        }
      }
    }
  }
}
```


