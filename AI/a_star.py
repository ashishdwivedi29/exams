import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbour, cost in graph[current]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(open_list, (new_f, new_g, neighbour, path + [neighbour]))

    return None, float('inf')

# 👇 User input for graph
graph = {}
n = int(input("Enter number of nodes in the graph: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbours = input(f"Enter neighbours of {node} (format: B,2 C,3): ")

    pairs = neighbours.split()
    graph[node] = []
    for p in pairs:
        neigh, cost = p.split(',')
        graph[node].append((neigh, int(cost)))


#  User input for heuristic
heuristic = {}
for node in graph.keys():
    h = int(input(f"Enter heuristic value for node {node}: "))
    heuristic[node] = h

#  Start and Goal
start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

# Run A* algorithm

path, cost = a_star(graph, start_node, goal_node, heuristic)

if path:
    print("Shortest path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found.")























# Enter number of nodes in the graph: 6
# Enter node name: A
# Enter neighbours of A (format: B,2 C,3): B,1 C,3
# Enter node name: B
# Enter neighbours of B (format: B,2 C,3): D,4 E,2
# Enter node name: C
# Enter neighbours of C (format: B,2 C,3): E,1
# Enter node name: D
# Enter neighbours of D (format: B,2 C,3): 
# Enter node name: E
# Enter neighbours of E (format: B,2 C,3): F,2
# Enter node name: F
# Enter neighbours of F (format: B,2 C,3): 
# Enter heuristic value for node A: 5
# Enter heuristic value for node B: 4
# Enter heuristic value for node C: 2
# Enter heuristic value for node D: 6
# Enter heuristic value for node E: 1
# Enter heuristic value for node F: 0
# Enter start node: A
# Enter goal node: F

