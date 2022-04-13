def segtree(arr):
    n = len(arr)
    tree = [float('inf')] * (2 * n)
    for i in range(n):
        update(tree, i, arr[i], n)
    return tree


def update(tree, i, x, n):
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


# Test
arr = [1, 2, 3, 4, 5]
segtree = segtree(arr)
print(segtree)

update(segtree, 0, 2, len(arr))
print(segtree)

print(minimum(segtree, 3, 4, len(arr)))