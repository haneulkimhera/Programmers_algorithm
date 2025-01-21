N, M = map(int,input().split())

def dfs(start,depth,path):
    if depth == M:
        print(*path)
        return

    for i in range(start,N+1):
        dfs(i,depth+1,path+[i])

dfs(1,0,[])