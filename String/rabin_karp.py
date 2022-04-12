def Rabin_Karp(s, p):
    """
    s: string
    p: pattern

    returns the list of indices where p is found in s
    """
    if len(p) > len(s):
        return -1
    if len(p) == 0:
        return 0
    if len(p) == 1:
        return s.find(p)
    # preprocessing
    p_hash = 0
    s_hash = 0
    for i in range(len(p)):
        p_hash = (p_hash * 256 + ord(p[i])) % (10 ** 9 + 7)
        s_hash = (s_hash * 256 + ord(s[i])) % (10 ** 9 + 7)
    
    ret = []
    # search
    for i in range(len(s) - len(p) + 1):
        if p_hash == s_hash:
            if p == s[i:i + len(p)]:
                ret.append(i)
        if i < len(s) - len(p):
            s_hash = (s_hash - ord(s[i]) * (256 ** (len(p) - 1))) * 256 + ord(s[i + len(p)])
            s_hash = s_hash % (10 ** 9 + 7)
    return ret


# Test
print(Rabin_Karp("Hello, my name is Hello", "Hello"))