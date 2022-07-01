# KMP

## Code

```python
def failure_function(p):
    l_pattern = len(p)
    table = [0] * l_pattern
    i = 1
    length = 0
    while i < l_pattern:
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
    l_text = len(s)
    l_pattern = len(p)
    ret = []
    while i < l_text:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = table[j - 1]
        if j == l_pattern:
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

Firstly, get a table by implementing failure functon.

```python
def failure_function(p):
    l_pattern = len(p)
    table = [0] * l_pattern
    i = 1
    length = 0
    while i < l_pattern:
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
```

Next, implement KMP.

```python
def KMP(s, p):
    table = failure_function(p)

    i = 0 # goes through the text
    j = 0 # goes through the pattern

    l_text = len(s)
    l_pattern = len(p)

    ret = []

    while i < l_text:

        # Matched
        if s[i] == p[j]:
            i += 1
            j += 1

        #unmatched
        else:
            # if j == 0, move i to the next character
            if j == 0:
                i += 1
            # otherwise, move j to the next character
            else:
                j = table[j - 1]

        # if j == l_pattern, then we found a match
        if j == l_pattern:
            ret.append(i - j)
            j = table[j - 1]

    return ret
```