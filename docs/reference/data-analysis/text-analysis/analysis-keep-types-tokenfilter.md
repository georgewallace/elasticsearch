---
navigation_title: "Keep types"
---

# Keep types token filter [analysis-keep-types-tokenfilter]


Keeps or removes tokens of a specific type. For example, you can use this filter to change `3 quick foxes` to `quick foxes` by keeping only `<ALPHANUM>` (alphanumeric) tokens.

::::{admonition} Token types
:class: note

Token types are set by the [tokenizer](analysis-tokenizers.md) when converting characters to tokens. Token types can vary between tokenizers.

For example, the [`standard`](analysis-standard-tokenizer.md) tokenizer can produce a variety of token types, including `<ALPHANUM>`, `<HANGUL>`, and `<NUM>`. Simpler analyzers, like the [`lowercase`](analysis-lowercase-tokenizer.md) tokenizer, only produce the `word` token type.

Certain token filters can also add token types. For example, the [`synonym`](analysis-synonym-tokenfilter.md) filter can add the `<SYNONYM>` token type.

Some tokenizers don’t support this token filter, for example keyword, simple_pattern, and simple_pattern_split tokenizers, as they don’t support setting the token type attribute.

::::


This filter uses Lucene’s [TypeTokenFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/core/TypeTokenFilter.md).

## Include example [analysis-keep-types-tokenfilter-analyze-include-ex]

The following [analyze API](indices-analyze.md) request uses the `keep_types` filter to keep only `<NUM>` (numeric) tokens from `1 quick fox 2 lazy dogs`.

```console
GET _analyze
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "keep_types",
      "types": [ "<NUM>" ]
    }
  ],
  "text": "1 quick fox 2 lazy dogs"
}
```

The filter produces the following tokens:

```text
[ 1, 2 ]
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens": [
%     {
%       "token": "1",
%       "start_offset": 0,
%       "end_offset": 1,
%       "type": "<NUM>",
%       "position": 0
%     },
%     {
%       "token": "2",
%       "start_offset": 12,
%       "end_offset": 13,
%       "type": "<NUM>",
%       "position": 3
%     }
%   ]
% }
% --------------------------------------------------


## Exclude example [analysis-keep-types-tokenfilter-analyze-exclude-ex]

The following [analyze API](indices-analyze.md) request uses the `keep_types` filter to remove `<NUM>` tokens from `1 quick fox 2 lazy dogs`. Note the `mode` parameter is set to `exclude`.

```console
GET _analyze
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "keep_types",
      "types": [ "<NUM>" ],
      "mode": "exclude"
    }
  ],
  "text": "1 quick fox 2 lazy dogs"
}
```

The filter produces the following tokens:

```text
[ quick, fox, lazy, dogs ]
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens": [
%     {
%       "token": "quick",
%       "start_offset": 2,
%       "end_offset": 7,
%       "type": "<ALPHANUM>",
%       "position": 1
%     },
%     {
%       "token": "fox",
%       "start_offset": 8,
%       "end_offset": 11,
%       "type": "<ALPHANUM>",
%       "position": 2
%     },
%     {
%       "token": "lazy",
%       "start_offset": 14,
%       "end_offset": 18,
%       "type": "<ALPHANUM>",
%       "position": 4
%     },
%     {
%       "token": "dogs",
%       "start_offset": 19,
%       "end_offset": 23,
%       "type": "<ALPHANUM>",
%       "position": 5
%     }
%   ]
% }
% --------------------------------------------------


## Configurable parameters [analysis-keep-types-tokenfilter-configure-parms]

`types`
:   (Required, array of strings) List of token types to keep or remove.

`mode`
:   (Optional, string) Indicates whether to keep or remove the specified token types. Valid values are:

    `include`
    :   (Default) Keep only the specified token types.

    `exclude`
    :   Remove the specified token types.



## Customize and add to an analyzer [analysis-keep-types-tokenfilter-customize]

To customize the `keep_types` filter, duplicate it to create the basis for a new custom token filter. You can modify the filter using its configurable parameters.

For example, the following [create index API](indices-create-index.md) request uses a custom `keep_types` filter to configure a new [custom analyzer](analysis-custom-analyzer.md). The custom `keep_types` filter keeps only `<ALPHANUM>` (alphanumeric) tokens.

```console
PUT keep_types_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "standard",
          "filter": [ "extract_alpha" ]
        }
      },
      "filter": {
        "extract_alpha": {
          "type": "keep_types",
          "types": [ "<ALPHANUM>" ]
        }
      }
    }
  }
}
```


