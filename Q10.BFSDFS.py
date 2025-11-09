# Graph Traversal using DFS (Adjacency Matrix) and BFS (Adjacency List)
# No imports used, simple and clear

# ---------- DFS Function ----------
def dfs(matrix, visited, start):
    print(nodes[start], end=" ")
    visited[start] = True
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(matrix, visited, i)

# ---------- BFS Function ----------
def bfs(adj_list, start):
    visited = [False] * len(adj_list)
    queue = [start]
    visited[start] = True

    while queue:
        curr = queue.pop(0)
        print(nodes[curr], end=" ")
        for neighbor in adj_list[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# ---------- MAIN PROGRAM ----------
n = int(input("Enter number of locations: "))
nodes = []

print("\nEnter location names:")
for i in range(n):
    name = input(f"Location {i+1}: ")
    nodes.append(name)

print("\nEnter the adjacency matrix (row by row):")
matrix = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

# Create adjacency list for BFS
adj_list = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            adj_list[i].append(j)
print(adj_list)

# Choose starting node
start_node = int(input(f"\nEnter starting node index (0 to {n-1}): "))

print("\nDFS Traversal (using Adjacency Matrix):")
visited = [False] * n
dfs(matrix, visited, start_node)

print("\n\nBFS Traversal (using Adjacency List):")
bfs(adj_list, start_node)
