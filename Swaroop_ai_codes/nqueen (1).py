N=int(input("enter number of queens : "))
b= [[0]*N for i in range(N)]

def printboard(b):
    for i in b:
        print(i)

def is_safe(i,j):
    for p in range(N):
        if b[p][j]==1 or b[i][p]==1:
            return False

    for n in range(N):
        for m in range(N):
            if i+j==n+m or i-j==n-m:
                if b[n][m]==1:
                    return False

    return True


def nqueen(noq):
    if noq==0:
        return True
    for i in range(N):
        for j in range(N):
            if b[i][j] != 1 and is_safe(i,j):
                b[i][j]=1
                if nqueen(noq-1)==True:
                    return True
                b[i][j]=0

    return False

if nqueen(N):
    printboard(b);
else:
    print("no solution exists")
