---
navigation_title: "Whitespace"
---

# Whitespace tokenizer [analysis-whitespace-tokenizer]


The `whitespace` tokenizer breaks text into terms whenever it encounters a whitespace character.


## Example output [_example_output_19] 

```console
POST _analyze
{
  "tokenizer": "whitespace",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

% 
% [source,console-result]
% ----------------------------
% {
%   "tokens": [
%     {
%       "token": "The",
%       "start_offset": 0,
%       "end_offset": 3,
%       "type": "word",
%       "position": 0
%     },
%     {
%       "token": "2",
%       "start_offset": 4,
%       "end_offset": 5,
%       "type": "word",
%       "position": 1
%     },
%     {
%       "token": "QUICK",
%       "start_offset": 6,
%       "end_offset": 11,
%       "type": "word",
%       "position": 2
%     },
%     {
%       "token": "Brown-Foxes",
%       "start_offset": 12,
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
%       "token": "dog’s",
%       "start_offset": 45,
%       "end_offset": 50,
%       "type": "word",
%       "position": 8
%     },
%     {
%       "token": "bone.",
%       "start_offset": 51,
%       "end_offset": 56,
%       "type": "word",
%       "position": 9
%     }
%   ]
% }
% ----------------------------
% 

The above sentence would produce the following terms:

```text
[ The, 2, QUICK, Brown-Foxes, jumped, over, the, lazy, dog's, bone. ]
```


## Configuration [_configuration_22] 

The `whitespace` tokenizer accepts the following parameters:

`max_token_length`
:   The maximum token length. If a token is seen that exceeds this length then it is split at `max_token_length` intervals. Defaults to `255`.

