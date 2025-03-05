---
navigation_title: "Truncate"
---

# Truncate token filter [analysis-truncate-tokenfilter]


Truncates tokens that exceed a specified character limit. This limit defaults to `10` but can be customized using the `length` parameter.

For example, you can use the `truncate` filter to shorten all tokens to `3` characters or fewer, changing `jumping fox` to `jum fox`.

This filter uses Lucene’s [TruncateTokenFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/miscellaneous/TruncateTokenFilter.md).

## Example [analysis-truncate-tokenfilter-analyze-ex]

The following [analyze API](indices-analyze.md) request uses the `truncate` filter to shorten tokens that exceed 10 characters in `the quinquennial extravaganza carried on`:

```console
GET _analyze
{
  "tokenizer" : "whitespace",
  "filter" : ["truncate"],
  "text" : "the quinquennial extravaganza carried on"
}
```

The filter produces the following tokens:

```text
[ the, quinquenni, extravagan, carried, on ]
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens" : [
%     {
%       "token" : "the",
%       "start_offset" : 0,
%       "end_offset" : 3,
%       "type" : "word",
%       "position" : 0
%     },
%     {
%       "token" : "quinquenni",
%       "start_offset" : 4,
%       "end_offset" : 16,
%       "type" : "word",
%       "position" : 1
%     },
%     {
%       "token" : "extravagan",
%       "start_offset" : 17,
%       "end_offset" : 29,
%       "type" : "word",
%       "position" : 2
%     },
%     {
%       "token" : "carried",
%       "start_offset" : 30,
%       "end_offset" : 37,
%       "type" : "word",
%       "position" : 3
%     },
%     {
%       "token" : "on",
%       "start_offset" : 38,
%       "end_offset" : 40,
%       "type" : "word",
%       "position" : 4
%     }
%   ]
% }
% --------------------------------------------------


## Add to an analyzer [analysis-truncate-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the `truncate` filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

```console
PUT custom_truncate_example
{
  "settings" : {
    "analysis" : {
      "analyzer" : {
        "standard_truncate" : {
        "tokenizer" : "standard",
        "filter" : ["truncate"]
        }
      }
    }
  }
}
```


## Configurable parameters [analysis-truncate-tokenfilter-configure-parms]

`length`
:   (Optional, integer) Character limit for each token. Tokens exceeding this limit are truncated. Defaults to `10`.


## Customize [analysis-truncate-tokenfilter-customize]

To customize the `truncate` filter, duplicate it to create the basis for a new custom token filter. You can modify the filter using its configurable parameters.

For example, the following request creates a custom `truncate` filter, `5_char_trunc`, that shortens tokens to a `length` of `5` or fewer characters:

```console
PUT 5_char_words_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "lowercase_5_char": {
          "tokenizer": "lowercase",
          "filter": [ "5_char_trunc" ]
        }
      },
      "filter": {
        "5_char_trunc": {
          "type": "truncate",
          "length": 5
        }
      }
    }
  }
}
```


