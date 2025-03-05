---
navigation_title: "Stop"
---

# Stop analyzer [analysis-stop-analyzer]


The `stop` analyzer is the same as the [`simple` analyzer](analysis-simple-analyzer.md) but adds support for removing stop words. It defaults to using the `_english_` stop words.


## Example output [_example_output_5] 

```console
POST _analyze
{
  "analyzer": "stop",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

% 
% [source,console-result]
% ----------------------------
% {
%   "tokens": [
%     {
%       "token": "quick",
%       "start_offset": 6,
%       "end_offset": 11,
%       "type": "word",
%       "position": 1
%     },
%     {
%       "token": "brown",
%       "start_offset": 12,
%       "end_offset": 17,
%       "type": "word",
%       "position": 2
%     },
%     {
%       "token": "foxes",
%       "start_offset": 18,
%       "end_offset": 23,
%       "type": "word",
%       "position": 3
%     },
%     {
%       "token": "jumped",
%       "start_offset": 24,
%       "end_offset": 30,
%       "type": "word",
%       "position": 4
%     },
%     {
%       "token": "over",
%       "start_offset": 31,
%       "end_offset": 35,
%       "type": "word",
%       "position": 5
%     },
%     {
%       "token": "lazy",
%       "start_offset": 40,
%       "end_offset": 44,
%       "type": "word",
%       "position": 7
%     },
%     {
%       "token": "dog",
%       "start_offset": 45,
%       "end_offset": 48,
%       "type": "word",
%       "position": 8
%     },
%     {
%       "token": "s",
%       "start_offset": 49,
%       "end_offset": 50,
%       "type": "word",
%       "position": 9
%     },
%     {
%       "token": "bone",
%       "start_offset": 51,
%       "end_offset": 55,
%       "type": "word",
%       "position": 10
%     }
%   ]
% }
% ----------------------------
% 

The above sentence would produce the following terms:

```text
[ quick, brown, foxes, jumped, over, lazy, dog, s, bone ]
```


## Configuration [_configuration_6] 

The `stop` analyzer accepts the following parameters:

`stopwords`
:   A pre-defined stop words list like `_english_` or an array containing a list of stop words. Defaults to `_english_`.

`stopwords_path`
:   The path to a file containing stop words. This path is relative to the Elasticsearch `config` directory.

See the [Stop Token Filter](analysis-stop-tokenfilter.md) for more information about stop word configuration.


## Example configuration [_example_configuration_5] 

In this example, we configure the `stop` analyzer to use a specified list of words as stop words:

```console
PUT my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_stop_analyzer": {
          "type": "stop",
          "stopwords": ["the", "over"]
        }
      }
    }
  }
}

POST my-index-000001/_analyze
{
  "analyzer": "my_stop_analyzer",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

% 
% [source,console-result]
% ----------------------------
% {
%   "tokens": [
%     {
%       "token": "quick",
%       "start_offset": 6,
%       "end_offset": 11,
%       "type": "word",
%       "position": 1
%     },
%     {
%       "token": "brown",
%       "start_offset": 12,
%       "end_offset": 17,
%       "type": "word",
%       "position": 2
%     },
%     {
%       "token": "foxes",
%       "start_offset": 18,
%       "end_offset": 23,
%       "type": "word",
%       "position": 3
%     },
%     {
%       "token": "jumped",
%       "start_offset": 24,
%       "end_offset": 30,
%       "type": "word",
%       "position": 4
%     },
%     {
%       "token": "lazy",
%       "start_offset": 40,
%       "end_offset": 44,
%       "type": "word",
%       "position": 7
%     },
%     {
%       "token": "dog",
%       "start_offset": 45,
%       "end_offset": 48,
%       "type": "word",
%       "position": 8
%     },
%     {
%       "token": "s",
%       "start_offset": 49,
%       "end_offset": 50,
%       "type": "word",
%       "position": 9
%     },
%     {
%       "token": "bone",
%       "start_offset": 51,
%       "end_offset": 55,
%       "type": "word",
%       "position": 10
%     }
%   ]
% }
% ----------------------------
% 

The above example produces the following terms:

```text
[ quick, brown, foxes, jumped, lazy, dog, s, bone ]
```


## Definition [_definition_5] 

It consists of:

Tokenizer
:   * [Lower Case Tokenizer](analysis-lowercase-tokenizer.md)


Token filters
:   * [Stop Token Filter](analysis-stop-tokenfilter.md)


If you need to customize the `stop` analyzer beyond the configuration parameters then you need to recreate it as a `custom` analyzer and modify it, usually by adding token filters. This would recreate the built-in `stop` analyzer and you can use it as a starting point for further customization:

```console
PUT /stop_example
{
  "settings": {
    "analysis": {
      "filter": {
        "english_stop": {
          "type":       "stop",
          "stopwords":  "_english_" <1>
        }
      },
      "analyzer": {
        "rebuilt_stop": {
          "tokenizer": "lowercase",
          "filter": [
            "english_stop"          <2>
          ]
        }
      }
    }
  }
}
```

%  TEST[s/\n$/\nstartyaml\n  - compare_analyzers: {index: stop_example, first: stop, second: rebuilt_stop}\nendyaml\n/]

1. The default stopwords can be overridden with the `stopwords` or `stopwords_path` parameters.
2. You’d add any token filters after `english_stop`.


