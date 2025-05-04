# Function to find parent of a node
def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])  # Path compression
    return parent[node]

# Function to perform union of two sets
def union(parent, u, v):
    root_u = find_parent(parent, u)
    root_v = find_parent(parent, v)
    if root_u != root_v:
        parent[root_v] = root_u  # Merge the sets
        return True
    return False

# Kruskal's Algorithm
def kruskal(edges, vertices):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = {v: v for v in vertices}
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        print(f"\nConsidering edge {u}-{v} with weight {weight}")
        if union(parent, u, v):
            print(f"Edge {u}-{v} added to MST")
            mst.append((u, v, weight))
            total_cost += weight
        else:
            print(f"Edge {u}-{v} creates a cycle and is skipped")
        print(f"Current parent set: {parent}")

    return mst, total_cost

# ----------------- Input from User -----------------

# Number of vertices
n = int(input("Enter the number of vertices: "))
vertices = []
print("Enter the vertex labels:")
for i in range(n):
    v = input().strip()
    vertices.append(v)

# Number of edges
e = int(input("Enter the number of edges: "))
edges = []
print("Enter each edge in the format: vertex1 vertex2 weight")
for _ in range(e):
    u, v, w = input().split()
    edges.append((u, v, int(w)))

# Run Kruskal's Algorithm
mst, cost = kruskal(edges, vertices)

# Output
print("\nMinimum Spanning Tree edges:")
for u, v, w in mst:
    print(f"{u} - {v} (Weight: {w})")
print("Total Cost:", cost)













# Enter the number of vertices: 4
# Enter the vertex labels:
# A
# B
# C
# D
# Enter the number of edges: 5
# Enter each edge in the format: vertex1 vertex2 weight
# A B 1
# B C 2
# A C 3
# A D 4
# C D 5
