def LPS_generator(pattern):
    """
    Generate the LPS array
    """
    l_pattern = len(pattern)
    LPS = [0] * l_pattern
    i = 1
    length = 0
    while i < l_pattern:
        if pattern[i] == pattern[length]:
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


def KMP(pattern, passage):
    LPS = LPS_generator(pattern)
    i = 0
    j = 0
    l_passage = len(passage)
    l_pattern = len(pattern)
    while i < l_passage:
        if passage[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = LPS[j - 1]
        if j == l_pattern:
            yield i - j + 1 #  The index of the word
            j = LPS[j - 1]
