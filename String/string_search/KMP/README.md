# KMP

## Code

```python
def failure_function(p):
    len_p = len(p)
    table = [0] * len_p
    i = 1
    j = 0

    # match
    while i < len_p:
        if p[i] == p[j]:
            j += 1
            table[i] = j
            i += 1
        else:
            if j > 0:
                j = table[j - 1]
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
    i = 1 # table[i]
    j = 0 # pointer to the same word

    while i < len_p:
        # match
        if p[i] == p[j]:
            j += 1
            table[i] = j
            i += 1

        # mismatch
        else:
            if j > 0:
                j = table[j - 1]
            else:
                table[i] = 0
                i += 1
    return table
```

It's basically running the KMP algorithm where both `s` and `p` are the pattern. `i` begins from `0` since the first letter can't have a proper suffix.

Let's take a closer look at the loop.

```python
    while i < len_p:
        # match
        if p[i] == p[j]:
            j += 1
            table[i] = j
            i += 1

        # mismatch
        else:
            if j == 0:
                table[i] = 0
                i += 1
            else:
                j = table[j - 1]
```

If a match occurs,, `j` is incremented first and put in `table[i]`. And then `i` is incremented for the next search.

If a mismatch occurs:

1. If `j == 0`—no previously matched characters—then `table[i] = 0` and `i` is incremented to continue matching.
2. If `j > 0`—there are previously matched characters—then `j = table[j - 1]` because there's still a possibility the prefix matches a shorter part of the pattern. Let's look at an example where `p = 'abebcdababe'` and `i == 10`, `j == 4`.

Here, `p[i]` is `'e'`, and `p[j]` is `'c'`.

|   |   |   |   |   |   |   |   |   |   | * |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | c | d | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">a</span> | <span style="color:blue">b</span> | e |
|   |   |   |   |   |   | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">a</span> | <span style="color:blue">b</span> | c | d | a | b | a | b | e |

A mismatch occured. Since there are previously matched characters `"abab"`, there's still a possibility `p[0:i + 1]` has a proper suffix. Do `j = table[j - 1] (which is 2)` and continue matching.

|   |   |   |   |   |   |   |   |   |   | * |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | c | d | a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | e |
|   |   |   |   |   |   |   |   | <span style="color:blue">a</span> | <span style="color:blue">b</span> | a | b | c | d | a | b | a | b | e |

Still a mismatch. Since `j == 2`, do `j = table[j - 1] (which is 0)` and continue matching.

|   |   |   |   |   |   |   |   |   |   | * |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | c | d | a | b | a | b | e |
|   |   |   |   |   |   |   |   |   |   | a | b | a | b | c | d | a | b | a | b | e |

Mismatch again. Since `j == 0`, there's no more possibility `p[0:i + 1]` has a proper suffix. So `table[i] = 0` and `i` is incremented to continue matching.

We couldn't take advantage of using the "KMP algorithm" to make a table here, but you could see what unnecessary steps can be skipped to find a table.