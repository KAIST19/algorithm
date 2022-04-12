def find_root(parent, i):
    """
    parent: list
    i: int
    """
    if parent[i] == i:
        return i
    parent[i] = find_root(parent, parent[i])
    return parent[i]


def union(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# Test
n = 10
parent = [i for i in range(n)]
union(parent, 1, 2)
print(parent)