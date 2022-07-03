# Kruskal's algorithm

## Code
```python
def kruskal(v, e, queue):
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
```

## Arguments & Return

- v: # of vertices
- e: # of edges
- queue: list of (a, b, cost) with $1 \leq a, b \leq v$
- returns ret, the least cost needed to form the minimum spanning tree.

## How it works

This algorithm uses the Disjoint-set data structure (aka union-find). The function `find_root` and `union` are the operations of it.

```python
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
```

Next, `queue` is sorted in descending order of the cost so that the smallest cost edge pops out.

```python
queue.sort(key=lambda x: x[2], reverse=True) # reversed so that the smallest pops out.
parent = [i for i in range(v + 1)]
ret = 0 # the total cost
```

Until `queue` is empty, the algorithm pops out the smallest cost edge and add it to the set. If either of the two vertices of the edge is already in the set, the algorithm ignores the edge.

```python
while queue:
    a, b, cost = queue.pop()
    if find_root(a) != find_root(b):
        union(a, b)
        ret += cost
```