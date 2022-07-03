# Shortest Path Problem

The shortest path problem is the problem of finding the path between two vertices in a graph such that the sum of the weights of the edges on the path is minimized.

## Single-source shortest paths

| Algorithm | Time Complexity | Weight | Directed | Cyclic |
| :---------: | :--------------: | :------: | :--------: | :------: |
| BFS | $O(V+E)$ | none | doesn't matter | detects cycles |
| Dijkstra's | $O(V^2)$ | R<sub>+</sub> | doesn't matter | no negative cycles |
| Topological Sort | $O(V+E)$ | | O | X |
| Bellman-Ford | $O(VE)$ | R | O | detects cycle |


## All-pairs shortest paths

| Algorithm | Time Complexity | Weight | Directed | Cyclic |
| :---------: | :--------------: | :------: | :--------: | :------: |
| Floyd-Warshall | $O(V^3)$ | R<sub>+</sub> | X | X |
| Floyd-WArshall | $O(V^3)$ | R | O | no negative cycles |