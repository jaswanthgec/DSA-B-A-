def dfs(graph, start, visited=None):
    """
    Perform depth-first search on a graph.

    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start: Starting node for DFS.
    visited (set): Set of visited nodes.

    Returns:
    list: List of nodes in the order they were visited.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

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
result = dfs(graph, start_node)
print(f"DFS starting from node {start_node}: {result}")
