def minKey(key, mstSet, n):
    min_val = float('inf')
    min_index = -1
    for v in range(n):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

def prim(graph, n):
    key = [float('inf')] * n
    parent = [-1] * n
    mstSet = [False] * n

    key[0] = 0

    for _ in range(n):
        u = minKey(key, mstSet, n)
        mstSet[u] = True
        for v in range(n):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    total_weight = 0
    print("\nPizza delivery path:")
    for i in range(1, n):
        print(f"Location {parent[i]} → Location {i} = {graph[i][parent[i]]}")
        total_weight += graph[i][parent[i]]
    print("Minimum total delivery time:", total_weight)

if _name_ == "_main_":
    print("Welcome to Pizza Delivery Route Optimizer!")
    n = int(input("Enter number of locations: "))
    graph = []

    print("Enter the adjacency matrix (travel times between locations):")
    print("If no direct path exists, enter 0.")
    for i in range(n):
        row_input = input(f"Row {i}: ").split()
        row = []
        for item in row_input:
            row.append(int(item))
        while len(row) != n:
            print(f"Please enter exactly {n} values for this row.")
            row_input = input(f"Row {i}: ").split()
            row = []
            for item in row_input:
                row.append(int(item))
        graph.append(row)

    prim(graph, n)



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
