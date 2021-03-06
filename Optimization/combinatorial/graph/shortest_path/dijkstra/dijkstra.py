"""
Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks.
"""
import heapq


def dijkstra(v, e, start, graph):
    """
    v: int
        1) number of vertices
    e: int
        1) number of edges
    s: int
        1) start point
        2) 1 <= s <= v
    graph: list
        1) adjacency list
        2) graph[i] contains tuples (j, cost) (1 <= i, j <= v)
    
    returns
    minimum: list
        1) minimum[i] is the minimum distance from the start point to vertex i (i = 1, ..., v)
        2) minimum[i] = float('inf') if there is no path from the start point to vertex i
    """

    minimum = [float('inf')] * (v + 1)
    minimum[start] = 0

    # initiates the priority queue
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_cost, current_node = heapq.heappop(queue)
        for next_cost, next_node in graph[current_node]:
            if next_cost + current_cost < minimum[next_node]:
                minimum[next_node] = next_cost + current_cost
                heapq.heappush(queue, (next_cost + current_cost, next_node))
    
    return minimum