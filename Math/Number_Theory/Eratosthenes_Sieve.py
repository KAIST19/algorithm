def Eratosthenes_Sieve(max_n):
    '''
    max_n: int
    '''
    sieve = [False, False] + [True] * (max_n - 1)
    for i in range(2, max_n + 1):
        if sieve[i]:
            for j in range(2 * i, max_n + 1, i):
                sieve[j] = False
    return sieve
