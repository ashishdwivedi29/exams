import heapq

g={}
e=int(input("enter the number of edges : "))
for i in range (e):
    a,b,weight=input().strip().split(" ")
    weight=int(weight)
    if g.get(a)==None:
        g[a]=[]
    g[a].append((b,weight))
    if g.get(b) == None:
        g[b] = []
    g[b].append((a, weight))


print(g)
"""
A B 2
A D 5
B C 1
B D 3
C D 4

"""
def prims(graph):
    # Initialize variables
    mst = []  # Stores the edges of the MST
    visited = set()  # Tracks visited nodes
    heap = []  # Priority queue for edges

    # Start with the first node in the graph
    start_node = list(graph.keys())[0]
    visited.add(start_node)

    # Add all edges from the start node to the heap
    for neighbor, weight in graph[start_node]:
        heapq.heappush(heap, (weight, start_node, neighbor))





    # Main algorithm loop
    while heap and len(visited) < len(graph):

        weight, u, v = heapq.heappop(heap)
        print(weight, u, v)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            # Add all edges from the new node to the heap
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(heap, (weight, v, neighbor))


    return mst



#
# g = {
#     'A': [('B', 2), ('D', 5)],
#     'B': [('A', 2), ('C', 1), ('D', 3)],
#     'C': [('B', 1), ('D', 4)],
#     'D': [('A', 5), ('B', 3), ('C', 4)]
# }
mst = prims(g)

print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(f"{edge[0]} -- {edge[1]} (weight: ({edge[2]})")
total_weight=0
for edge in mst:
    total_weight+=int(edge[2])
print(f"\nTotal weight of MST: {total_weight}")
