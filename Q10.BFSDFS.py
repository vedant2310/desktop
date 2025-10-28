# Graph traversal example:
# Nodes: A, B, C, D, E, F
# Edges (undirected): A-B, A-C, B-D, B-E, C-F, E-F

from collections import deque

# --- Setup: nodes and edges (you can change these) ---
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
index = {node: i for i, node in enumerate(nodes)}   # map node -> index
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('E', 'F')
]

# --- Build adjacency list (for BFS) ---
adj_list = {node: [] for node in nodes}
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)   # undirected graph

# (optional) sort neighbors for deterministic traversal order
for node in adj_list:
    adj_list[node].sort()

# --- Build adjacency matrix (for DFS) ---
n = len(nodes)
adj_matrix = [[0]*n for _ in range(n)]
for u, v in edges:
    i, j = index[u], index[v]
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1


# ---------------- BFS (using adjacency list) ----------------
def bfs(start):
    visited = {node: False for node in nodes}
    order = []
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        u = q.popleft()
        order.append(u)
        # traverse neighbors in sorted order (if you want deterministic output)
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return order


# ---------------- DFS (using adjacency matrix) ----------------
def dfs_util(u_idx, visited, order):
    visited[u_idx] = True
    order.append(nodes[u_idx])
    # explore neighbors by index order (A->B->C...)
    for v_idx in range(n):
        if adj_matrix[u_idx][v_idx] == 1 and not visited[v_idx]:
            dfs_util(v_idx, visited, order)


def dfs(start):
    visited = [False]*n
    order = []
    start_idx = index[start]
    dfs_util(start_idx, visited, order)
    return order


# ---------------- Run (starting from 'A') ----------------
start_node = 'A'
bfs_order = bfs(start_node)
dfs_order = dfs(start_node)

print("Adjacency List (for BFS):")
for node in nodes:
    print(f" {node} -> {adj_list[node]}")

print("\nAdjacency Matrix (for DFS):")
for i,row in enumerate(adj_matrix):
    print(f" {nodes[i]}: {row}")

print(f"\nBFS visit order starting from {start_node}: {bfs_order}")
print(f"DFS visit order starting from {start_node}: {dfs_order}")




Algorithm: Graph Traversal using BFS and DFS

Start with a set of popular locations (A, B, C, …) as nodes of a graph.

Represent the routes between locations as edges connecting nodes.

Create an Adjacency List for performing BFS.

Create an Adjacency Matrix for performing DFS.

Choose a starting node (say, A).

For BFS:

-Initialize a queue and a visited list.

-Visit the start node, enqueue it, and mark as visited.

-Repeatedly dequeue a node, visit all unvisited adjacent nodes, and enqueue them.

For DFS:

-Use recursion or a stack with the adjacency matrix.

-Visit the starting node, mark as visited.

-Recursively visit all its unvisited adjacent nodes.

Display the order of traversal for both BFS and DFS.

End.