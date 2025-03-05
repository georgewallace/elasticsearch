---
navigation_title: "KStem"
---

# KStem token filter [analysis-kstem-tokenfilter]


Provides [KStem](https://ciir.cs.umass.edu/pubfiles/ir-35.pdf)-based stemming for the English language. The `kstem` filter combines [algorithmic stemming](stemming.md#algorithmic-stemmers) with a built-in [dictionary](stemming.md#dictionary-stemmers).

The `kstem` filter tends to stem less aggressively than other English stemmer filters, such as the [`porter_stem`](analysis-porterstem-tokenfilter.md) filter.

The `kstem` filter is equivalent to the [`stemmer`](analysis-stemmer-tokenfilter.md) filter’s [`light_english`](analysis-stemmer-tokenfilter.md#analysis-stemmer-tokenfilter-language-parm) variant.

This filter uses Lucene’s [KStemFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/en/KStemFilter.md).

## Example [analysis-kstem-tokenfilter-analyze-ex]

The following analyze API request uses the `kstem` filter to stem `the foxes jumping quickly` to `the fox jump quick`:

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "kstem" ],
  "text": "the foxes jumping quickly"
}
```

The filter produces the following tokens:

```text
[ the, fox, jump, quick ]
```

% [source,console-result]
% ----
% {
%   "tokens": [
%     {
%       "token": "the",
%       "start_offset": 0,
%       "end_offset": 3,
%       "type": "<ALPHANUM>",
%       "position": 0
%     },
%     {
%       "token": "fox",
%       "start_offset": 4,
%       "end_offset": 9,
%       "type": "<ALPHANUM>",
%       "position": 1
%     },
%     {
%       "token": "jump",
%       "start_offset": 10,
%       "end_offset": 17,
%       "type": "<ALPHANUM>",
%       "position": 2
%     },
%     {
%       "token": "quick",
%       "start_offset": 18,
%       "end_offset": 25,
%       "type": "<ALPHANUM>",
%       "position": 3
%     }
%   ]
% }
% ----


## Add to an analyzer [analysis-kstem-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the `kstem` filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

::::{important} 
To work properly, the `kstem` filter requires lowercase tokens. To ensure tokens are lowercased, add the [`lowercase`](analysis-lowercase-tokenfilter.md) filter before the `kstem` filter in the analyzer configuration.

::::


```console
PUT /my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "whitespace",
          "filter": [
            "lowercase",
            "kstem"
          ]
        }
      }
    }
  }
}
```


