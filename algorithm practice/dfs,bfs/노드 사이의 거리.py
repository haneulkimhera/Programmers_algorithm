from collections import deque

n, m = map(int,input().split())

graph = [[]*(n+1) for _ in range(n+1)]
for i in range(n-1):
    node1, node2, dist = map(int,input().split())
    graph[node1].append((node2,dist))
    graph[node2].append((node1,dist))

# print()
# for i in range(1,n+1):
#     print(graph[i][1:5])

def dfs(start,end):
    visited = [0]*(n+1)
    queue = deque()
    visited[start] = 1
    queue.append((start,0))

    while(queue):
        curr,dist = queue.popleft()
        if curr == end:
            return dist
        for next, l in graph[curr]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append((next,dist+l))

for i in range(m):
    node1, node2 = map(int,input().split())
    dist = dfs(node1,node2)
    print(dist)