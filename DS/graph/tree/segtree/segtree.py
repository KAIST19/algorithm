def segtree(arr):
    n = len(arr)
    tree = [0] * (2 * n)
    for i in range(n):
        update(tree, i, arr[i], n)
    return tree


def update(tree, i, x, n):
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


def partial_sum(tree, i, j, n):
    """
    partial sum of [i, j]
    0 <= i <= j < n
    """
    i += n
    j += n
    res = 0
    while i <= j:
        if i % 2 == 1:
            res += tree[i]
            i += 1
        if j % 2 == 0:
            res += tree[j]
            j -= 1
        i //= 2
        j //= 2
    return res


# Test
arr = [1, 2, 3, 4, 5]
segtree = segtree(arr)
print(segtree)

update(segtree, 0, 1, len(arr))
print(segtree)

print(partial_sum(segtree, 0, 1, len(arr)))