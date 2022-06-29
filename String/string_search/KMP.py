def fail_function(p):
    """
    Generate the LPS array
    """
    l_pattern = len(p)
    LPS = [0] * l_pattern
    i = 1
    length = 0
    while i < l_pattern:
        if p[i] == p[length]:
            length += 1
            LPS[i] = length
            i += 1
        else:
            if length > 0:
                length = LPS[length - 1]
            else:
                LPS[i] = 0
                i += 1
    return LPS


def KMP(s, p):
    """
    returns the list of indices where the pattern p is found in the string s
    beginning from 0
    """
    LPS = fail_function(p)
    i = 0
    j = 0
    l_passage = len(s)
    l_pattern = len(p)
    ret = []
    while i < l_passage:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = LPS[j - 1]
        if j == l_pattern:
            ret.append(i - j)
            j = LPS[j - 1]
    return ret

print(KMP("Hello, my name is name", "name"))