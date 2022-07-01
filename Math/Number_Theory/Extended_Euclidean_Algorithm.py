# Returns the gcd of two integers and the solutions
def EEA(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = EEA(b % a, a)
        return gcd, y - (b // a) * x, x
