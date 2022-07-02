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

Prior to searching, the pattern is preprocessed by a function called "failure function" which returns a table.

The table is a list of integers. The definition is as follows.

`table[i]` = the longest prefix of `p[0:i+1]` that is also the suffix of `p[0:i+1]`.

For example, the table of `AABAACAABAA` would be:
| A | A | B | A | A | C | A | A | B | A | A |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 2 | 0 | 1 | 2 | 3 | 4 | 5 |

Here, table[4] would be 2 because `p[0:5] = AABAA` and the longest prefix (and suffix) would be `AA`.

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
            # if length > 0, then we can set length to table[length - 1] since the longest prefix of p[0:length] is also a suffix of p[0:length]
            if length > 0:
                length = table[length - 1]
            else:
                table[i] = 0
                i += 1
    return table
```

Next, implement KMP. It uses the same algorithm as the failure function.

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

The table belows depicts the process of finding `abcabb` from the text `ababcababbaab`. The asterisk * shows where the comparison occurs.
|   |   |   |   |   |   |   | * |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">a</span> | b | b | a | a | b |
|   |   | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> |<span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">b</span> |   |

Oops, there's a mismatch.

The naive algorithm would just do `i += 1` and resume its comparison from the beginning of the pattern. This table below shows the next step in this case.

|   |   |   | * |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | c | a | b | a | b | b | a | a | b |
|   |   |   | a | b | c |a | b | b |   |

On the other hand, the KMP algorithm looks into the first 5 letters to see what can be skipped.

|   |   |   |   |   |   |   | * |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> | <span style="color:blue">A</span> | <span style="color:blue">B</span> | <span style="color:red">a</span> | b | b | a | a | b |
|   |   | <span style="color:blue">A</span> | <span style="color:blue">B</span> | <span style="color:blue">c</span> |<span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">b</span> |   |

**The key idea here is that a match won't occur until the `AB` of the pattern gets to the `AB` of the text.** The comparison inbetween can be skipped.

|   |   |   |   |   |   |   | * |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">a</span> | b | b | a | a | b |
|   |   |   |   |   | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> |<span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">b</span> |   |

and here's the code that does it.

```python
length = table[length - 1]
```
Note that `i` doesn't change.