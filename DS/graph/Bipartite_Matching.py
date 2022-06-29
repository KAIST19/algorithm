def bipartite_matching(n, m, graph):
    """
    n: int
        1) number of nodes in the domain
    m: int
        2) number of nodes in the range
    graph: list of list containing which element is to connected to which

    returns
    ret: a list where ret[i] is the index of the element in the domain \
        that chose i-th element 
    """
    def dfs(i):
        if visited[i]:
            return False
        visited[i] = True
        for choice in graph[i]:
            if ret[choice] == -1 or dfs(ret[choice]):
                ret[choice] = i
                return True
        return False

    ret = [-1] * m

    for i in range(n):
        visited = [False] * n
        dfs(i)

    return ret