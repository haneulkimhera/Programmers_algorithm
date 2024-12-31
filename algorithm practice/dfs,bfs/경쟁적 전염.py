from collections import deque

n,k = map(int,input().split())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))

s,x,y = map(int,input().split())

queue = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            queue.append((j,i,board[i][j]))
queue = deque(sorted(queue, key=lambda x: x[2]))
# print(f"queue: {queue}\n")

def spread(queue,s,dest_x,dest_y):
    seconds = -1
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while(queue):
        seconds += 1
        # print(f"second: {seconds}")
        # print("-----------")
        # for i in range(n):
        #     print(board[i])
        # print("-----------")
        if seconds == s:
            return board[dest_x-1][dest_y-1]
        queue = deque(sorted(queue, key=lambda x: x[2]))
        for _ in range(len(queue)):
            x,y,virus = queue.popleft()
            # print(f"({x},{y}) >>>")
            for dx,dy in direction:
                x_ = x+dx
                y_ = y+dy
                # print(f"x_:{x_} y_:{y_}, board[y_][x_]:{board[y_][x_]}")
                if (0<=x_<n and 0<=y_<n) and (board[y_][x_]==0):
                    board[y_][x_] = virus
                    queue.append((x_,y_,virus))
    return board[dest_x-1][dest_y-1]

print(spread(queue,s,x,y))



