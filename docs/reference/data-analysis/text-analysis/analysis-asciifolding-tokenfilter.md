---
navigation_title: "ASCII folding"
---

# ASCII folding token filter [analysis-asciifolding-tokenfilter]


Converts alphabetic, numeric, and symbolic characters that are not in the Basic Latin Unicode block (first 127 ASCII characters) to their ASCII equivalent, if one exists. For example, the filter changes `à` to `a`.

This filter uses Lucene’s [ASCIIFoldingFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/miscellaneous/ASCIIFoldingFilter.md).

## Example [analysis-asciifolding-tokenfilter-analyze-ex]

The following [analyze API](indices-analyze.md) request uses the `asciifolding` filter to drop the diacritical marks in `açaí à la carte`:

```console
GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : ["asciifolding"],
  "text" : "açaí à la carte"
}
```

The filter produces the following tokens:

```text
[ acai, a, la, carte ]
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens" : [
%     {
%       "token" : "acai",
%       "start_offset" : 0,
%       "end_offset" : 4,
%       "type" : "<ALPHANUM>",
%       "position" : 0
%     },
%     {
%       "token" : "a",
%       "start_offset" : 5,
%       "end_offset" : 6,
%       "type" : "<ALPHANUM>",
%       "position" : 1
%     },
%     {
%       "token" : "la",
%       "start_offset" : 7,
%       "end_offset" : 9,
%       "type" : "<ALPHANUM>",
%       "position" : 2
%     },
%     {
%       "token" : "carte",
%       "start_offset" : 10,
%       "end_offset" : 15,
%       "type" : "<ALPHANUM>",
%       "position" : 3
%     }
%   ]
% }
% --------------------------------------------------


## Add to an analyzer [analysis-asciifolding-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the `asciifolding` filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

```console
PUT /asciifold_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_asciifolding": {
          "tokenizer": "standard",
          "filter": [ "asciifolding" ]
        }
      }
    }
  }
}
```


## Configurable parameters [analysis-asciifolding-tokenfilter-configure-parms]

`preserve_original`
:   (Optional, Boolean) If `true`, emit both original tokens and folded tokens. Defaults to `false`.


## Customize [analysis-asciifolding-tokenfilter-customize]

To customize the `asciifolding` filter, duplicate it to create the basis for a new custom token filter. You can modify the filter using its configurable parameters.

For example, the following request creates a custom `asciifolding` filter with `preserve_original` set to true:

```console
PUT /asciifold_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_asciifolding": {
          "tokenizer": "standard",
          "filter": [ "my_ascii_folding" ]
        }
      },
      "filter": {
        "my_ascii_folding": {
          "type": "asciifolding",
          "preserve_original": true
        }
      }
    }
  }
}
```


