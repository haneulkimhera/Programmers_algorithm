N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

stack = []
for i in range(N):
    for j in range(M):
        stack.append((i,j))

d_move = [(1,0),(-1,0),(0,1),(0,-1)]

total = []

def dfs(x,y):
    nth = 1
    sum = board[y][x]
    stack = [(x,y,nth,sum)]
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1

    while(stack):
        x,y,n,sum = stack.pop()

        if n==4:
            total.append(sum)
            continue

        for dx,dy in d_move:
            x_ = x+dx
            y_ = y+dy
            if (0<=x_<M and 0<=y_<N) and (visited[y_][x_]==0):
                visited[y_][x_] = 1
                stack.append((x_,y_,n+1,sum+board[y_][x_]))

for i in range(N):
    for j in range(M):
        dfs(i,j)

total = sorted(total,reverse=True)

print(total[0])