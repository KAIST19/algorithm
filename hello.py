"""
DS that can efficiently update elements and calculate prefix sums in a table of numbers.
"""
def getsum(BITTree, i):
    """
    BITTree: list
        1) the tree returned from construct()
    i: int
        1) the index of the element to get the sum of
        2) 0 <= i < len(BITTree)
    """
    s = 0
    i += 1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s


def updatebit(BITTree, n, i, v):
    """
    BITTree: list
        1) the tree returned from construct()
    n: int
        1) the length of the array
        2) n = len(BITTree) - 1
    i: int
        1) the index of the element to update
        2) 0 <= i < n
    v: int
        1) the value to add to the element at index i
    """
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)


def construct(arr):
    n = len(arr)
    BITTree = [0] * (n + 1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
BITTree = construct(arr)
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    print(getsum(BITTree, b) - getsum(BITTree, a - 1))