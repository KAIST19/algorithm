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
    j = 0
    len_s = len(s)
    len_p = len(p)
    ret = []
    while i < len_s:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = table[j - 1]
        if j == len_p:
            ret.append(i - j)
            j = table[j - 1]
    return ret
```

## Arguments & Return

### failure function

- p: pattern

### KMP

- s: string
- p: pattern
- rerturns ret: list of indices(starting from 0) where the pattern "p"s are found in the text s

## How it works
> [Visualization](https://cmps-people.ok.ubc.ca/ylucet/DS/KnuthMorrisPratt.html)

Firstly, get a table by implementing failure functon.

Here, `table[i]` = the longest prefix of `p[0:i+1]` that is also a suffix of `p[0:i+1]`. 

Example:
| A | A | B | A | A | C | A | A | B | A | A |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 2 | 0 | 1 | 2 | 3 | 4 | 5 |

```python
def failure_function(p):
    len_p = len(p)
    table = [0] * len_p
    i = 1
    length = 0

    while i < len_p:
        # matched
        if p[i] == p[length]:
            length += 1
            table[i] = length
            i += 1

        # unmatched
        else:
            # if length > 0, then we can set length to table[length - 1] since the longest prefix of p[0:length] is also a suffix of p[0:length]
            if length > 0:
                length = table[length - 1]
            else:
                table[i] = 0
                i += 1
    return table
```

Next, implement KMP.

```python
def KMP(s, p):
    table = failure_function(p)

    i = 0 # goes through the text
    j = 0 # goes through the pattern

    len_s = len(s)
    len_p = len(p)

    ret = []

    while i < len_s:

        # matched
        if s[i] == p[j]:
            i += 1
            j += 1

        # unmatched
        else:
            # if j == 0, move i to the next character
            if j == 0:
                i += 1
            # otherwise, move j to the next character
            else:
                j = table[j - 1]

        # if j == len_p, then we found a match
        if j == len_p:
            ret.append(i - j)
            j = table[j - 1]

    return ret
```