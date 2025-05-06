import heapq
g={}
e= int(input("enter the number of edges : "))
for i in range(e):
    a,b,weight = input().strip().split(" ") #A B 5
    weight = int(weight)  # ✅ this is the fix

    if g.get(a)==None:
        g[a]=[]
    g[a].append((b,weight))
    if g.get(b)==None:
        g[b]=[]
    g[b].append((a,weight))

def a_star(graph,start,goal,heuristic):
    open_list=[]
    heapq.heappush(open_list,(heuristic[start],0,start,[start]))
    visited=[]
    while open_list:
        f,g_cost,current,path=heapq.heappop(open_list)

        if current==goal:
            return path,g_cost

        if current in visited:
            continue
        else :
            visited.append(current)

        for neightbour,cost in g[current]:
            if neightbour not in visited:
                new_g=cost+g_cost
                new_f= new_g + heuristic[neightbour]
                heapq.heappush(open_list,(new_f,new_g,neightbour,path+[neightbour]))
    return None,float('inf')




heuristic={}
print("enter the heuristic values : ")
for node in g:
    heuristic[node] = int(input(f"enter the heuristic value for {node} : "))

start=input("enter the start node : ")
goal=input("enter the goal node : ")

path,cost=a_star(g,start,goal,heuristic)
if path:
    print("shortest path :","->".join(path))
    print("total cost : ",cost)
else :
    print("no path found")

"""
A B 1
A C 4
B C 2
B D 5
C D 1
"""