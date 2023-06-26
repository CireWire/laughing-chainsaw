#!/usr/bin/env python



import heapq

"""
__author__ = "CireWire"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "dreaded.sushi@gmail.com"
__status__ = "Production"
"""

def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding the shortest paths in a weighted graph.

    Args:
        graph (dict): The graph represented as an adjacency dictionary.
                      Each key is a vertex, and the value is a dictionary
                      mapping neighboring vertices to their associated edge weights.
        start (object): The starting vertex.

    Returns:
        dict: A dictionary containing the shortest distances from the start vertex
              to all other vertices in the graph.

    Raises:
        ValueError: If the start vertex is not present in the graph.
    """
    if start not in graph:
        raise ValueError("Start vertex is not present in the graph.")

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignore outdated entries
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 6},
    'D': {'B': 3, 'C': 6}
}

try:
    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)

    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"To vertex {vertex}: {distance}")

except ValueError as e:
    print(f"Error: {e}")
