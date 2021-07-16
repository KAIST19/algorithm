def power(base, exponent, mod):
    if exponent == 1:
        return base
    elif exponent == 0:
        return 1
    elif exponent % 2 == 0:
        ret = power(base, exponent // 2, mod)
        return ret ** 2 % mod
    else:
        return power(base, exponent - 1, mod) * base


def binary_coefficient(n, k, mod):
    numerator, denominator = 1, 1
    for i in range(1, n + 1):
        numerator *= i
        numerator %= mod
    for i in range(1, k + 1):
        denominator *= i
        denominator %= mod
    for i in range(1, n - k + 1):
        denominator *= i
        denominator %= mod

    denominator = power(denominator, mod - 2, mod) % mod
    return numerator * denominator % mod
