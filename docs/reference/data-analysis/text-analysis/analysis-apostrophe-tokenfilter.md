---
navigation_title: "Apostrophe"
---

# Apostrophe token filter [analysis-apostrophe-tokenfilter]


Strips all characters after an apostrophe, including the apostrophe itself.

This filter is included in {{es}}'s built-in [Turkish language analyzer](analysis-lang-analyzer.md#turkish-analyzer). It uses Lucene’s [ApostropheFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/tr/ApostropheFilter.md), which was built for the Turkish language.

## Example [analysis-apostrophe-tokenfilter-analyze-ex]

The following [analyze API](indices-analyze.md) request demonstrates how the apostrophe token filter works.

```console
GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : ["apostrophe"],
  "text" : "Istanbul'a veya Istanbul'dan"
}
```

The filter produces the following tokens:

```text
[ Istanbul, veya, Istanbul ]
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens" : [
%     {
%       "token" : "Istanbul",
%       "start_offset" : 0,
%       "end_offset" : 10,
%       "type" : "<ALPHANUM>",
%       "position" : 0
%     },
%     {
%       "token" : "veya",
%       "start_offset" : 11,
%       "end_offset" : 15,
%       "type" : "<ALPHANUM>",
%       "position" : 1
%     },
%     {
%       "token" : "Istanbul",
%       "start_offset" : 16,
%       "end_offset" : 28,
%       "type" : "<ALPHANUM>",
%       "position" : 2
%     }
%   ]
% }
% --------------------------------------------------


## Add to an analyzer [analysis-apostrophe-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the apostrophe token filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

```console
PUT /apostrophe_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_apostrophe": {
          "tokenizer": "standard",
          "filter": [ "apostrophe" ]
        }
      }
    }
  }
}
```


