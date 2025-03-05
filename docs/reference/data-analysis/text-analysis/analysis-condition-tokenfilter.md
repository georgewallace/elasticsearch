---
navigation_title: "Conditional"
---

# Conditional token filter [analysis-condition-tokenfilter]


Applies a set of token filters to tokens that match conditions in a provided predicate script.

This filter uses Lucene’s [ConditionalTokenFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/miscellaneous/ConditionalTokenFilter.md).

## Example [analysis-condition-analyze-ex]

The following [analyze API](indices-analyze.md) request uses the `condition` filter to match tokens with fewer than 5 characters in `THE QUICK BROWN FOX`. It then applies the [`lowercase`](analysis-lowercase-tokenfilter.md) filter to those matching tokens, converting them to lowercase.

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "condition",
      "filter": [ "lowercase" ],
      "script": {
        "source": "token.getTerm().length() < 5"
      }
    }
  ],
  "text": "THE QUICK BROWN FOX"
}
```

The filter produces the following tokens:

```text
[ the, QUICK, BROWN, fox ]
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens" : [
%     {
%       "token" : "the",
%       "start_offset" : 0,
%       "end_offset" : 3,
%       "type" : "<ALPHANUM>",
%       "position" : 0
%     },
%     {
%       "token" : "QUICK",
%       "start_offset" : 4,
%       "end_offset" : 9,
%       "type" : "<ALPHANUM>",
%       "position" : 1
%     },
%     {
%       "token" : "BROWN",
%       "start_offset" : 10,
%       "end_offset" : 15,
%       "type" : "<ALPHANUM>",
%       "position" : 2
%     },
%     {
%       "token" : "fox",
%       "start_offset" : 16,
%       "end_offset" : 19,
%       "type" : "<ALPHANUM>",
%       "position" : 3
%     }
%   ]
% }
% --------------------------------------------------


## Configurable parameters [analysis-condition-tokenfilter-configure-parms]

`filter`
:   (Required, array of token filters) Array of token filters. If a token matches the predicate script in the `script` parameter, these filters are applied to the token in the order provided.

These filters can include custom token filters defined in the index mapping.


`script`
:   (Required, [script object](modules-scripting-using.md)) Predicate script used to apply token filters. If a token matches this script, the filters in the `filter` parameter are applied to the token.

For valid parameters, see [*How to write scripts*](modules-scripting-using.md). Only inline scripts are supported. Painless scripts are executed in the [analysis predicate context](https://www.elastic.co/guide/en/elasticsearch/painless/current/painless-analysis-predicate-context.html) and require a `token` property.



## Customize and add to an analyzer [analysis-condition-tokenfilter-customize]

To customize the `condition` filter, duplicate it to create the basis for a new custom token filter. You can modify the filter using its configurable parameters.

For example, the following [create index API](indices-create-index.md) request uses a custom `condition` filter to configure a new [custom analyzer](analysis-custom-analyzer.md). The custom `condition` filter matches the first token in a stream. It then reverses that matching token using the [`reverse`](analysis-reverse-tokenfilter.md) filter.

```console
PUT /palindrome_list
{
  "settings": {
    "analysis": {
      "analyzer": {
        "whitespace_reverse_first_token": {
          "tokenizer": "whitespace",
          "filter": [ "reverse_first_token" ]
        }
      },
      "filter": {
        "reverse_first_token": {
          "type": "condition",
          "filter": [ "reverse" ],
          "script": {
            "source": "token.getPosition() === 0"
          }
        }
      }
    }
  }
}
```


