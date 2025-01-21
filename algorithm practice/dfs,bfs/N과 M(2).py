def dfs(depth, start, path):
    if depth == M:
        print(*path)
        return
    
    for i in range(start, N + 1):
        dfs(depth + 1, i + 1, path + [i])

N, M = map(int, input().split())

dfs(0, 1, [])