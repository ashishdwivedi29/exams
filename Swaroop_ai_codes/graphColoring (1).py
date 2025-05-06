# def make_even(marks):
#     if marks>=90:
#         return 'O'
#     elif 90>marks and marks>80:
#         return 'A'
#     elif 80 > marks and marks > 70:
#         return 'B'
#     elif 70 > marks and marks > 60:
#         return 'C'
#     elif 60 > marks and marks > 50:
#         return 'D'
#     else :
#         return 'Fail'
#
# marks=[90,85,75,65,55,10]
#
# y=list(map(make_even,marks))
# print(y)
g={}
m=int(input("enter number of colors you want to use for the coloring the graph: "))
e=int(input("enter the number of edges : "))
for i in range(e):
    a,b= map(int,input().split(" ")) #0 1
    if g.get(a)==None:
        g[a]=[]
    g[a].append(b)
    if g.get(b)==None:
        g[b]=[]
    g[b].append(a)

"""
3
6
0 1
0 2
0 3
1 2
2 3
3 4
"""
v=len(g.keys())
posCol=["red","green","violet","blue","yellow","orange","indigo"]
def canColor(g,col,n,colList):
    for child in g[n]:
        if colList[child]== posCol[col]:
            return False
    return True

def graphColoring(g,m,n,v,colList):  #{1:red,2:blue}
    if n==v:
        return True

    for col in range(m):
        if canColor(g,col,n,colList):
            colList[n]= posCol[col]
            if graphColoring(g,m,n+1,v,colList):
                return True
            colList[n]=-1

    return False

colList={}
for i in g.keys():
    colList[i]=-1
print(g)

if graphColoring(g,m,0,v,colList):
    print(colList)
else:
    print(f"can't color the graph with m{m} colors")


