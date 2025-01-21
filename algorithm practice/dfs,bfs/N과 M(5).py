N, M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
visited = [False] * N

def dfs(visited,depth,path):
    if depth==M:
        print(*path)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(visited, depth + 1, path + [numbers[i]])
            visited[i] = False

dfs(visited,0,[])