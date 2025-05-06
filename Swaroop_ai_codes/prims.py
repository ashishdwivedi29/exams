import heapq
g={}
e=int(input("enter the number of edges : "))
for i in range(e):
    a,b,weight=input().strip().split(" ")
    weight=int(weight)
    if g.get(a)==None:
        g[a]=[]
    g[a].append((b,weight))
    if g.get(b)==None:
        g[b]=[]
    g[b].append((a,weight))

def prims(graph,start):
    mst=[]
    open_list=[]
    visited=[]
    visited.append(start)

    for n,w in graph[start]:
        heapq.heappush(open_list,(w,start,n))

    while open_list and len(visited)<len(graph):
        w,u,v=heapq.heappop(open_list)
        if v not in visited:
            visited.append(v)
            mst.append((u,v,w))
            for n,w in graph[v]:
                if n not in visited:
                    heapq.heappush(open_list,(w,v,n))

    return mst
start=input("enter the start node")
mst=prims(g,start)

print("the minimum spanning tree edges are : ")

for edge in mst:
    print(f"{edge[0]} -- {edge[1]} (weight : {edge[2]})")


total_weight=0
for edge in mst:
    total_weight+=edge[2]
print(f"\nTotal weight of MST: {total_weight}")

"""
A B 2
A D 5
B C 1
B D 3
C D 4
"""