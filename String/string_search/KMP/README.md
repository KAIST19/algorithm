# KMP

## Code

```python
def failure_function(p):
    len_p = len(p)
    table = [0] * len_p
    i = 1
    length = 0

    # match
    while i < len_p:
        if p[i] == p[length]:
            length += 1
            table[i] = length
            i += 1
        else:
            if length > 0:
                length = table[length - 1]
            else:
                table[i] = 0
                i += 1
    return table


def KMP(s, p):
    table = failure_function(p)
    i = 0
    length = 0
    len_s = len(s)
    len_p = len(p)
    ret = []
    while i < len_s:
        if s[i] == p[length]:
            i += 1
            length += 1
        else:
            if length == 0:
                i += 1
            else:
                length = table[length - 1]
        if length == len_p:
            ret.append(i - length)
            length = table[length - 1]
    return ret
```

## Arguments & Return

### failure function

- p: pattern

### KMP

- s: text
- p: pattern
- rerturns ret: list of indices(starting from 0) where the pattern "p"s are found in the text

## How it works
> [Visualization](https://cmps-people.ok.ubc.ca/ylucet/DS/KnuthMorrisPratt.html)

### Overview

The KMP algorithm is a string search algorithm. It takes a test `s` and a pattern `p` and returns a list of indices where the pattern `p`s are found in the text `s`. Before searching, it preprocesses the pattern `p` to create `table` and use it to search the pattern `p` more efficiently.

### Preprocessing

Prior to searching, the pattern is preprocessed by a function called "failure function" which returns `table`.

`table` is a list containing integers, defined as follows.

`table[i]` = the longest prefix of `p[0:i+1]` that is also the suffix of `p[0:i+1]`.

For instance, `table` of `"abcabb"` would be:
| a | b | c | a | b | b |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 2 | 0 |

Here, `table[4] == 2` because `p[0:5] = "abcab"` and the longest prefix (and suffix) is `"ab"`.

`failure_function` is a function that takes a pattern `p` and returns a `table`. We're gonna talk about it later on. Let's first look at how the KMP algorithm works, assuming `failure_function` is given.

### KMP algorithm
Here is a KMP function which takes a text `s` and a pattern `p` and returns a list of indices where the pattern `p`s are found in the text `s`.

```python
def KMP(s, p):
    table = failure_function(p)

    i = 0 # i-th letter in s is compared.
    length = 0 # length-th letter in p is compared.

    len_s = len(s)
    len_p = len(p)

    ret = []

    while i < len_s:
        # match
        if s[i] == p[length]:
            i += 1
            length += 1

        # mismatch
        else:
            # if length == 0, move i to the next character
            if length == 0:
                i += 1
            # otherwise, move length to the next character
            else:
                length = table[length - 1]

        # if length == len_p, then we found a match
        if length == len_p:
            ret.append(i - length)
            length = table[length - 1]

    return ret
```

What's different from the naive algorithm is that when a mismatch occurs, it takes the most efficient move, eliminating unnecessary steps. Let's see how it works.

The table belows depicts the process of finding `"abcabb"` from the text `"ababcababbaab"`. The asterisk * shows where the comparison occurs.
|   |   |   |   |   |   |   | * |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">a</span> | b | b | a | a | b |
|   |   | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> |<span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">b</span> |   |

Oops, a mismatch.

The naive algorithm would just do `i += 1` and resume its comparison from the beginning of the pattern. This table would be like this:

|   |   |   | * |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | c | a | b | a | b | b | a | a | b |
|   |   |   | a | b | c |a | b | b |   |

On the other hand, the KMP algorithm looks into the first 5 letters of the pattern—`"abcab"`—to see what can be skipped.

|   |   |   |   |   |   |   | * |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> | <span style="color:blue">A</span> | <span style="color:blue">B</span> | <span style="color:red">a</span> | b | b | a | a | b |
|   |   | <span style="color:blue">A</span> | <span style="color:blue">B</span> | <span style="color:blue">c</span> |<span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">b</span> |   |

**The key idea here is that a match won't occur until the `"AB"` of the pattern gets to the `"AB"` of the text.** The comparison inbetween can be skipped. Thus, the most efficient move is to move the pattern so that the `"AB"`s are put together as follows.

|   |   |   |   |   |   |   | * |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">a</span> | b | b | a | a | b |
|   |   |   |   |   | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> |<span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">b</span> |   |

`length = table[length - 1]` would do the job. `i` doesn't change. It could be a little tricky to understand, but recall that `i`, `length` are pointers to the letter being compared.

### Failure function

Now, let's see how `failure_function` works.

```python
def failure_function(p):
    len_p = len(p)
    table = [0] * len_p
    i = 1
    length = 0

    while i < len_p:
        # match
        if p[i] == p[length]:
            length += 1
            table[i] = length
            i += 1

        # mismatch
        else:
            if length > 0:
                length = table[length - 1]
            else:
                table[i] = 0
                i += 1
    return table
```

As you can see, it looks very similar to the KMP algorithm. We can use the same idea—skipping unnecessary steps steps—to get a table.

Consider implementing the KMP algorithm for `p == "ababcb"` and `s == "ababcb"`. Note that this time `i` starts from `1` since `table[0]` is always `0`.

> `i == 1` <br> `length == 0`

|   | * |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | c | b |   |   |   |   |   |
|   | a | b | a | b | c | b |   |   |   |   |
| 0 | 0 | 0 | 0 | 0 | 0 |   |   |   |   |   |

(the 0s on the bottom represnet the values of `table`)

Here, we're comparing the 1st letter of `s` with the 0th letter of `p`. It's a mismatch and `length == 0` so `table[1] = 0` and `i = 1 + 1`.

|   |   | * |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | c | b |   |   |   |   |   |
|   |   | a | b | a | b | c | b |   |   |   |
| 0 | 0 | 0 | 0 | 0 | 0 |   |   |   |   |   |

