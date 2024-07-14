from collections import deque

def bfs(graph, start):
    """
    Perform breadth-first search on a graph.

    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start: Starting node for BFS.

    Returns:
    list: List of nodes in the order they were visited.
    """
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'
result = bfs(graph, start_node)
print(f"BFS starting from node {start_node}: {result}")
