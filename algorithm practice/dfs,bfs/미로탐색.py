from collections import deque

n,m = map(int,input().split())

board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int,str(input())))

visited = [[0]*m for _ in range(n)]

def bfs(x,y):
    queue = deque()
    queue.append((x,y,1))
    x_dir=[1,-1,0,0]
    y_dir=[0,0,1,-1]
    visited[y][x]=1
    while(queue):
        x,y,cnt = queue.popleft()
        # print(f"x:{x},y:{y}, cnt:{cnt}")
        if (x,y)==(m-1,n-1):
            return cnt
        for i in range(4):
            x_ = x+x_dir[i]
            y_ = y+y_dir[i]
            if 0<=x_<m and 0<=y_<n:
                if board[y_][x_]==1 and visited[y_][x_]==0:
                    visited[y_][x_]=1
                    queue.append((x_,y_,cnt+1))

answer = bfs(0,0)

print(answer)