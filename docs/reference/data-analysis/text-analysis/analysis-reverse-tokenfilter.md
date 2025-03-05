---
navigation_title: "Reverse"
---

# Reverse token filter [analysis-reverse-tokenfilter]


Reverses each token in a stream. For example, you can use the `reverse` filter to change `cat` to `tac`.

Reversed tokens are useful for suffix-based searches, such as finding words that end in `-ion` or searching file names by their extension.

This filter uses Lucene’s [ReverseStringFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/reverse/ReverseStringFilter.md).

## Example [analysis-reverse-tokenfilter-analyze-ex]

The following [analyze API](indices-analyze.md) request uses the `reverse` filter to reverse each token in `quick fox jumps`:

```console
GET _analyze
{
  "tokenizer" : "standard",
  "filter" : ["reverse"],
  "text" : "quick fox jumps"
}
```

The filter produces the following tokens:

```text
[ kciuq, xof, spmuj ]
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens" : [
%     {
%       "token" : "kciuq",
%       "start_offset" : 0,
%       "end_offset" : 5,
%       "type" : "<ALPHANUM>",
%       "position" : 0
%     },
%     {
%       "token" : "xof",
%       "start_offset" : 6,
%       "end_offset" : 9,
%       "type" : "<ALPHANUM>",
%       "position" : 1
%     },
%     {
%       "token" : "spmuj",
%       "start_offset" : 10,
%       "end_offset" : 15,
%       "type" : "<ALPHANUM>",
%       "position" : 2
%     }
%   ]
% }
% --------------------------------------------------


## Add to an analyzer [analysis-reverse-tokenfilter-analyzer-ex]

The following [create index API](indices-create-index.md) request uses the `reverse` filter to configure a new [custom analyzer](analysis-custom-analyzer.md).

```console
PUT reverse_example
{
  "settings" : {
    "analysis" : {
      "analyzer" : {
        "whitespace_reverse" : {
          "tokenizer" : "whitespace",
          "filter" : ["reverse"]
        }
      }
    }
  }
}
```


