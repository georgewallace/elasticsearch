---
navigation_title: "Lowercase"
---

# Lowercase tokenizer [analysis-lowercase-tokenizer]


The `lowercase` tokenizer, like the [`letter` tokenizer](analysis-letter-tokenizer.md) breaks text into terms whenever it encounters a character which is not a letter, but it also lowercases all terms. It is functionally equivalent to the [`letter` tokenizer](analysis-letter-tokenizer.md) combined with the [`lowercase` token filter](analysis-lowercase-tokenfilter.md), but is more efficient as it performs both steps in a single pass.


## Example output [_example_output_12] 

```console
POST _analyze
{
  "tokenizer": "lowercase",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

% 
% [source,console-result]
% ----------------------------
% {
%   "tokens": [
%     {
%       "token": "the",
%       "start_offset": 0,
%       "end_offset": 3,
%       "type": "word",
%       "position": 0
%     },
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
%       "token": "the",
%       "start_offset": 36,
%       "end_offset": 39,
%       "type": "word",
%       "position": 6
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
[ the, quick, brown, foxes, jumped, over, the, lazy, dog, s, bone ]
```


## Configuration [_configuration_13] 

The `lowercase` tokenizer is not configurable.

