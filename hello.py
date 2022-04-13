def segtree_min(arr):
    n = len(arr)
    tree = [float('inf')] * (2 * n)
    for i in range(n):
        update_min(tree, i, arr[i], n)
    return tree


def segtree_partial_sum(arr):
    n = len(arr)
    tree = [0] * (2 * n)
    for i in range(n):
        update_partial_sum(tree, i, arr[i], n)
    return tree


def update_min(tree, i, x, n):
    """
    add x to i-th element
    i: int
        1) 0 <= i < n
    x: int/double
        1) change the value to x
    n: int
        1) size of arr
    """
    i += n
    tree[i] = x
    while i > 0:
        i //= 2
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])


def update_partial_sum(tree, i, x, n):
    """
    add x to i-th element
    i: int
        1) 0 <= i < n
    x: int/double
        1) x is added to i-th element
    n: int
        1) size of arr
    """
    i += n
    tree[i] += x
    while i > 0:
        i //= 2
        tree[i] += x


def minimum(tree, i, j, n):
    """
    minimum in [i, j]
    0 <= i <= j < n
    """
    i += n
    j += n
    ret = float('inf')
    while i <= j:
        if i % 2 == 1:
            ret = min(ret, tree[i])
            i += 1
        if j % 2 == 0:
            ret = min(ret, tree[j])
            j -= 1
        i //= 2
        j //= 2
    return ret


def partial_sum(tree, i, j, n):
    """
    partial sum of [i, j]
    0 <= i <= j < n
    """
    i += n
    j += n
    ret = 0
    while i <= j:
        if i % 2 == 1:
            ret += tree[i]
            i += 1
        if j % 2 == 0:
            ret += tree[j]
            j -= 1
        i //= 2
        j //= 2
    return ret


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
min_tree = segtree_min(arr)
partial_sum_tree = segtree_partial_sum(arr)

ret = 0
for i in range(n):
    for j in range(i, n):
        ret = max(ret, minimum(min_tree, i, j, n) * partial_sum(partial_sum_tree, i, j, n))
print(ret)