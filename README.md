# Dijkstra's Algorithm

This repository contains a Python implementation of Dijkstra's algorithm, which is used to find the shortest paths in a weighted graph.

## Usage

The `dijkstra` function in the `dijkstra.py` file implements Dijkstra's algorithm. It takes a graph represented as an adjacency dictionary and a start vertex as input, and returns a dictionary containing the shortest distances from the start vertex to all other vertices in the graph.

To use the algorithm, follow these steps:

1. Ensure you have Python installed on your machine.
2. Clone this repository or download the `dijkstra.py` file.
3. Import the `dijkstra` function in your Python script or interactive session.
4. Create a graph represented as an adjacency dictionary.
5. Call the `dijkstra` function with the graph and the start vertex as arguments.
6. Retrieve the shortest distances from the returned dictionary and process them as needed.

Here's an example of how to use the algorithm:

```python
from dijkstra import dijkstra

# Create a graph represented as an adjacency dictionary
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 6},
    'D': {'B': 3, 'C': 6}
}

# Set the start vertex
start_vertex = 'A'

# Find the shortest distances using Dijkstra's algorithm
distances = dijkstra(graph, start_vertex)

# Process the shortest distances as needed
for vertex, distance in distances.items():
    print(f"To vertex {vertex}: {distance}")
 ```

## Contributing
Contributions to improve the algorithm or add additional features are welcome. If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
