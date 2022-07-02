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

Next, implement KMP. It uses the same algorithm as the failure function.

```python
def KMP(s, p):
    table = failure_function(p)

    i = 0 # goes through the text
    length = 0 # goes through the pattern

    len_s = len(s)
    len_p = len(p)

    ret = []

    while i < len_s:

        # matched
        if s[i] == p[length]:
            i += 1
            length += 1

        # unmatched
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

The key idea is that even if the letter from the text doesn't match the letter from the pattern, we can still take advantage of the fact that **the length - 1 letters on the left were matched**.

In the table below, the letters from each were unmatched(<span style="color:red">red letters</span>). But the length - 1 letters on the left were matched. (<span style="color:blue">blue letters</span>) 

:warning: if you can't see 

| a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">a</span> | b | b | a | a | b |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> |<span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">b</span> |   |

Since `table[5]` = 2, the pattern can be shifted as follows.
| a | b | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">a</span> | b | b | a | a | b |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   | <span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:blue">c</span> |<span style="color:blue">a</span> | <span style="color:blue">b</span> | <span style="color:red">b</span> |   |

and here's the code that does it.

```python
length = table[length - 1]
```