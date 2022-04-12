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
n, q = map(int, input().split())
parent = [0 for _ in range(n + 1)]
parent[1] = 1
for i in range(2, n + 1):
    parent[i] = int(input())

queries = []
for _ in range(n - 1 + q):
    queries.append(tuple(map(int, input().split())))

parents = [i for i in range(n + 1)]
ret_stack = []

for _ in range(n - 1 + q):
    pop = queries.pop()
    if pop[0] == 0:
        union(parents, pop[1], parent[pop[1]])
    else:
        if find_root(parents, pop[1]) == find_root(parents, pop[2]):
            ret_stack.append(True)
        else:
            ret_stack.append(False)

for _ in range(q):
    if ret_stack.pop():
        print("YES")
    else:
        print("NO")