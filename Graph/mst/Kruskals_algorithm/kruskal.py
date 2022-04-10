"""
Kruskal's algorithm finds the minimum spanning forest of an UNDIRECTED edge-weighted graph.
"""
def kruskal(v, e, queue):
    """
    v: int
        1) number of vertices
    e: int
        1) number of edges
    queue: list
        1) a list consisting of (a, b, queue)
        2) 1 <= a, b <= v
    """

    def find_root(node):
        while node != parent[node]:
            node = parent[node]
        return node

    def union(a, b):
        a = find_root(a)
        b = find_root(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    queue.sort(key=lambda x: x[2], reverse=True) # reversed so that the smallest pops out.
    parent = [i for i in range(v + 1)]
    ret = 0 # the total cost

    while queue:
        a, b, cost = queue.pop()
        if find_root(a) != find_root(b):
            union(a, b)
            ret += cost

    return ret


# Test code
# v, e = map(int, input().split())
# queue = []
# for _ in range(e):
#     queue.append(tuple(map(int, input().split())))
# print(kruskal(v, e, queue))