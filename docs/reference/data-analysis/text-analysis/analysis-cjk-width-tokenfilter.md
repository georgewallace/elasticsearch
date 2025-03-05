---
navigation_title: "CJK width"
---

# CJK width token filter [analysis-cjk-width-tokenfilter]


Normalizes width differences in CJK (Chinese, Japanese, and Korean) characters as follows:

* Folds full-width ASCII character variants into the equivalent basic Latin characters
* Folds half-width Katakana character variants into the equivalent Kana characters

This filter is included in {{es}}'s built-in [CJK language analyzer](analysis-lang-analyzer.md#cjk-analyzer). It uses Lucene’s [CJKWidthFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/cjk/CJKWidthFilter.md).

::::{note} 
This token filter can be viewed as a subset of NFKC/NFKD Unicode normalization. See the [`analysis-icu` plugin](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu-normalization-charfilter.html) for full normalization support.
::::


## Example [analysis-cjk-width-tokenfilter-analyze-ex]

```console
GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : ["cjk_width"],
  "text" : "ｼｰｻｲﾄﾞﾗｲﾅｰ"
}
```

The filter produces the following token:

```text
シーサイドライナー
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens" : [
%     {
%       "token" : "シーサイドライナー",
%       "start_offset" : 0,
%       "end_offset" : 10,
%       "type" : "<KATAKANA>",
%       "position" : 0
%     }
%   ]
% }
% --------------------------------------------------


## Add to an analyzer [analysis-cjk-width-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the CJK width token filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

```console
PUT /cjk_width_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_cjk_width": {
          "tokenizer": "standard",
          "filter": [ "cjk_width" ]
        }
      }
    }
  }
}
```


