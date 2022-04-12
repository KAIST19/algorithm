def hash(s):
    p = 53 # small + large case (31 for small only)
    m = 1e9 + 9
    
    ret = 0
    power = 1
    
    for i in range(len(s)):
        ret = (ret + ord(s[i]) * power) % m
        power = (power * p) % m
    
    return ret