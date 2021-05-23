#  attempt to match n to m
#  returns True if
def dfs(n, visited, to_this):
    if visited[n] == 1:
        return False
    visited[n] = True
    for i in l[n]:
        if to_this[i] == 0 or dfs(to_this[i]):
            to_this[i] = n
            return True
    return False


def Bipartite_Matching():
    #  n: # of domain
    #  m: # of codomain
    n, m = map(int, input().split())
    # ith element of l contains probable tasks
    l = [[], ]
    #  t[x] = y: x matched to y
    to_this = [0] * (m + 1)
    #  tasks for each n
    for _ in range(n):
        l.append([int(i) for i in input().split()][1:])

    # for each i:
    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        dfs(i, visited, to_this)
    return to_this[1:]
