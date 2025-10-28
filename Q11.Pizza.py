# Graph using adjacency list
graph = {
    'Shop': {'A': 4, 'B': 2},
    'A': {'Shop': 4, 'C': 3, 'D': 5},
    'B': {'Shop': 2, 'C': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'A': 5, 'C': 4}
}

# Dijkstra’s Algorithm (simple version)
def shortest_time(graph, start):
    visited = []
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    while len(visited) < len(graph):
        # Find unvisited node with smallest distance
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or distance[node] < distance[min_node]:
                    min_node = node

        # Visit the node
        visited.append(min_node)

        # Update distances for its neighbors
        for neighbor, time in graph[min_node].items():
            if distance[min_node] + time < distance[neighbor]:
                distance[neighbor] = distance[min_node] + time

    return distance


# Starting point
result = shortest_time(graph, 'Shop')

# Display result
print("Minimum time from Shop to each location:")
for loc in result:
    print(f"{loc} : {result[loc]} minutes")



Algorithm: Minimum Pizza Delivery Time using Dijkstra’s Algorithm

Start

Represent delivery locations as a weighted graph using an adjacency list

Initialize all node distances as infinity, except the starting node (Shop = 0)

Mark all nodes as unvisited

Repeat until all nodes are visited:

-Select the unvisited node with the smallest distance value

-For each of its neighboring nodes:

--Calculate the new tentative distance

--If the new distance is smaller, update it

-Mark the current node as visited

Continue until all nodes have been processed

Display the shortest (minimum time) distance from the shop to each location

Stop