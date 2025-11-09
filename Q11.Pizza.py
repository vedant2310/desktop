V = int(input("Enter number of locations: "))

graph = []
print("Enter the adjacency matrix (row by row):")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

selected = [0]        # Start from A (index 0)
edges = []            # To store final edges
total = 0

while len(selected) < V:
    min_wt = 9999
    u = v = -1
    for i in selected:
        for j in range(V):
            if graph[i][j] != 0 and j not in selected and graph[i][j] < min_wt:
                min_wt = graph[i][j]
                u, v = i, j
    selected.append(v)
    edges.append((u, v, min_wt))
    total += min_wt

print("\nMinimum Spanning Tree:")
for u, v, w in edges:
    print(f"{chr(u+65)} - {chr(v+65)}  =  {w}")
print("Total Minimum Time:", total)
