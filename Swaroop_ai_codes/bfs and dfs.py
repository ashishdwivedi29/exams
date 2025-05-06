g={}
e=int(input("enter number of edges in the graph : "))
v=int(input("enter number of vertices in the graph : "))
for i in range(e):
    a,b=map(int,input().split(" "))
    if g.get(a)==None:
        g[a]=[]
    g[a].append(b)
    if g.get(b) == None:
        g[b] = []
    g[b].append(a)
visited=[]

def dfs_recursive(graph,vertex,visited):
    visited.append(vertex)
    print(vertex," ")
    for neighbour in g[vertex]:
        if neighbour not in visited:
            dfs_recursive(graph,neighbour,visited)

# dfs_recursive(g,0,visited)




"""
0 1
0 2
1 4
1 2
2 3
3 3
4 5
"""
queue=[]
def BFS_recursive(graph,queue,visited):

    if not queue:
        return

    vertex=queue.pop(0)
    if vertex not in visited:
        visited.append(vertex)
        print(vertex," ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
    BFS_recursive(graph,queue,visited)


start=int(input("enter the start node: "))
queue.append(start)
BFS_recursive(g,queue,visited)

# dfs_recursive(g,start,visited)