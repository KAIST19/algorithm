import sys
input = sys.stdin.readline


def floyd_warshall(v, d):
    for k in range(v):
        for a in range(v):
            for b in range(v):
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])
    
    return d


n = int(input())
d = [[float('inf')] * 52 for _ in range(52)]
for i in range(52):
    d[i][i] = 0

key = dict()
for i in range(26):
    key[chr(ord('A') + i)] = i
for i in range(26):
    key[chr(ord('a') + i)] = i + 26


for _ in range(n):
    line = input().split()
    a = key[line[0]]
    b = key[line[2]]
    d[a][b] = 1

for k in range(52):
    for a in range(52):
        for b in range(52):
            if d[a][b] > d[a][k] + d[k][b]:
                d[a][b] = d[a][k] + d[k][b]

ret = 0
for a in range(52):
    for b in range(52):
        if 0 < d[a][b] < float('inf'):
            ret += 1

print(ret)

for a in range(52):
    for b in range(52):
        if 0 < d[a][b] < float('inf'):
            if a < 26:
                print(chr(ord('A') + a), end = '')
            else:
                print(chr(ord('a') + a - 26), end = '')
            
            print(' => ', end = '')

            if b < 26:
                print(chr(ord('A') + b), end = '')
            else:
                print(chr(ord('a') + b - 26), end = '')
            print()
