# Floyd-Warshall Algorithm

## Code

```python
def floyd_warshall(v, d):
    for k in range(v):
        for a in range(v):
            for b in range(v):
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])
    
    return d
```

## Arguments & Return

- v: # of vertices
- d: adjacency matrix. Has `0` along the diagonal, `'inf'` if not connected.
- returns d, a matrix of minimum distances from each vertex to each vertex

## How it works

```python
def floyd_warshall(v, d):
    for k in range(v):
        for a in range(v):
            for b in range(v):
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])
    
    return d
```

Prior to the for loop, `d` only contains the distances with a single edge. The `for k in range(v)` loop adds the distances with multiple edges including the node k. For each iteration, all the elements in `d` are recalculated to see if there's a shorter path going through the node k.