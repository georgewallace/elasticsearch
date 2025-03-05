---
navigation_title: "Porter stem"
---

# Porter stem token filter [analysis-porterstem-tokenfilter]


Provides [algorithmic stemming](stemming.md#algorithmic-stemmers) for the English language, based on the [Porter stemming algorithm](https://snowballstem.org/algorithms/porter/stemmer.md).

This filter tends to stem more aggressively than other English stemmer filters, such as the [`kstem`](analysis-kstem-tokenfilter.md) filter.

The `porter_stem` filter is equivalent to the [`stemmer`](analysis-stemmer-tokenfilter.md) filter’s [`english`](analysis-stemmer-tokenfilter.md#analysis-stemmer-tokenfilter-language-parm) variant.

The `porter_stem` filter uses Lucene’s [PorterStemFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/en/PorterStemFilter.md).

## Example [analysis-porterstem-tokenfilter-analyze-ex]

The following analyze API request uses the `porter_stem` filter to stem `the foxes jumping quickly` to `the fox jump quickli`:

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "porter_stem" ],
  "text": "the foxes jumping quickly"
}
```

The filter produces the following tokens:

```text
[ the, fox, jump, quickli ]
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
%       "token": "quickli",
%       "start_offset": 18,
%       "end_offset": 25,
%       "type": "<ALPHANUM>",
%       "position": 3
%     }
%   ]
% }
% ----


## Add to an analyzer [analysis-porterstem-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the `porter_stem` filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

::::{important} 
To work properly, the `porter_stem` filter requires lowercase tokens. To ensure tokens are lowercased, add the [`lowercase`](analysis-lowercase-tokenfilter.md) filter before the `porter_stem` filter in the analyzer configuration.

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
            "porter_stem"
          ]
        }
      }
    }
  }
}
```


