# 백준 2606 - 바이러스 #

n=int(input())
v=int(input())
computers = [[0]*(n+1) for i in range(n+1)]
visited = [0]*(n+1)
for i in range(1,n+1):
    computers[i][i]=1

for i in range(v):
    a,b=map(int,input().split())
    computers[a][b]=1
    computers[b][a]=1


def solution(computers):
    global cnt 
    cnt = 0

    def dfs(node):
        global cnt
        for next in range(1,n+1):
            if computers[node][next]==1 and visited[next]==0:
                visited[next]=1
                cnt+=1
                dfs(next)

    dfs(1)
    return cnt

print(solution(computers)-1)

