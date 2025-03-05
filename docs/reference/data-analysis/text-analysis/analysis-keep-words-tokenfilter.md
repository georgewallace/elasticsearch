---
navigation_title: "Keep words"
---

# Keep words token filter [analysis-keep-words-tokenfilter]


Keeps only tokens contained in a specified word list.

This filter uses Lucene’s [KeepWordFilter](https://lucene.apache.org/core/10_1_0/analysis/common/org/apache/lucene/analysis/miscellaneous/KeepWordFilter.md).

::::{note} 
To remove a list of words from a token stream, use the [`stop`](analysis-stop-tokenfilter.md) filter.

::::


## Example [analysis-keep-words-tokenfilter-analyze-ex]

The following [analyze API](indices-analyze.md) request uses the `keep` filter to keep only the `fox` and `dog` tokens from `the quick fox jumps over the lazy dog`.

```console
GET _analyze
{
  "tokenizer": "whitespace",
  "filter": [
    {
      "type": "keep",
      "keep_words": [ "dog", "elephant", "fox" ]
    }
  ],
  "text": "the quick fox jumps over the lazy dog"
}
```

The filter produces the following tokens:

```text
[ fox, dog ]
```

% [source,console-result]
% --------------------------------------------------
% {
%   "tokens": [
%     {
%       "token": "fox",
%       "start_offset": 10,
%       "end_offset": 13,
%       "type": "word",
%       "position": 2
%     },
%     {
%       "token": "dog",
%       "start_offset": 34,
%       "end_offset": 37,
%       "type": "word",
%       "position": 7
%     }
%   ]
% }
% --------------------------------------------------


## Configurable parameters [analysis-keep-words-tokenfilter-configure-parms]

`keep_words`
:   (Required*, array of strings) List of words to keep. Only tokens that match words in this list are included in the output.

Either this parameter or `keep_words_path` must be specified.


`keep_words_path`
:   (Required*, array of strings) Path to a file that contains a list of words to keep. Only tokens that match words in this list are included in the output.

This path must be absolute or relative to the `config` location, and the file must be UTF-8 encoded. Each word in the file must be separated by a line break.

Either this parameter or `keep_words` must be specified.


`keep_words_case`
:   (Optional, Boolean) If `true`, lowercase all keep words. Defaults to `false`.


## Customize and add to an analyzer [analysis-keep-words-tokenfilter-customize]

To customize the `keep` filter, duplicate it to create the basis for a new custom token filter. You can modify the filter using its configurable parameters.

For example, the following [create index API](indices-create-index.md) request uses custom `keep` filters to configure two new [custom analyzers](analysis-custom-analyzer.md):

* `standard_keep_word_array`, which uses a custom `keep` filter with an inline array of keep words
* `standard_keep_word_file`, which uses a customer `keep` filter with a keep words file

```console
PUT keep_words_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_keep_word_array": {
          "tokenizer": "standard",
          "filter": [ "keep_word_array" ]
        },
        "standard_keep_word_file": {
          "tokenizer": "standard",
          "filter": [ "keep_word_file" ]
        }
      },
      "filter": {
        "keep_word_array": {
          "type": "keep",
          "keep_words": [ "one", "two", "three" ]
        },
        "keep_word_file": {
          "type": "keep",
          "keep_words_path": "analysis/example_word_list.txt"
        }
      }
    }
  }
}
```


