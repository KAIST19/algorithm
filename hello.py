import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    types = dict()
    n = int(input())
    for _ in range(n):
        b, a = input().split()
        if a in types:
            types[a] += 1
        else:
            types[a] = 1
    
    ans = 1
    for i in types.keys():
        ans *= (types[i] + 1)
    
    print(ans - 1)