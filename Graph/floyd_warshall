"""
The Floyd–Warshall finds the shortest paths in a directed weighted graph with positive or negative edge weights (but with no negative cycles).
"""
def floyd_warshall(n, d):
    """
    n: int
        1) # of vertices
    d: list
        1) adjacency matrix
        2) d[i][j] = distance(cost) from i to j (0 <= i, j < n)
        3) diagonal = zeros
        4) if connected, elements are costs. if not, elements are +inf
        5) negative cycles not allowed
    """

    for k in range(n):
        for a in range(n):
            for b in range(n):
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])
    
    return d
