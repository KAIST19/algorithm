# Dijkstra's algorithm

## Code

```python
import heapq


def dijkstra(v, e, start, graph):
   

    minimum = [float('inf')] * (v + 1)
    minimum[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_cost, current_node = heapq.heappop(queue)
        for next_cost, next_node in graph[current_node]:
            if next_cost + current_cost < minimum[next_node]:
                minimum[next_node] = next_cost + current_cost
                heapq.heappush(queue, (next_cost + current_cost, next_node))
    
    return minimum
```

## Arguments & Return

- v: # of vertices
- e: # of edges
- start: start point (1 <= start <= v)
- graph: adjacency list (graph[i] is a list containing (j, cost))
- returns minimum, a list of minimum distances from the start point to each vertex


## How it works

```python
import heapq


def dijkstra(v, e, start, graph):
   
    # initiates minimum with 'inf' in it.
    minimum = [float('inf')] * (v + 1)
    minimum[start] = 0

    # initiates priority queue with (0, start)
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        # pops the first element in the queue
        current_cost, current_node = heapq.heappop(queue)

        for next_cost, next_node in graph[current_node]:
            # if there's a shorter path to next_node, update minimum
            if next_cost + current_cost < minimum[next_node]:
                minimum[next_node] = next_cost + current_cost
                heapq.heappush(queue, (next_cost + current_cost, next_node))
    
    return minimum
```

`minimum` is a list of minimum distances from the start point to each vertex. It's initiated with `'inf'` in it except the start point which is `0`.

`queue` is a priority queue which pops out the elemenet with the smallest cost. It pops out the tuble with the smallest cost, and this is very similar to the BFS algorithm.

### BFS vs Dijkstra's algorithm

> The BFS algorithm guarantees that the current search has the shortest path. Revisiting the same node means it's gone through more nodes, which is why BFS never visits the same queue again.
> 
> On the other hand, there's no guarantee that the current search has the shortest path. A shorter path could be found for the same node when revisited through a different path. This is why the dijkstra's algorithm keeps searching until the queue is empty.