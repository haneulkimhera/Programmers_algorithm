from collections import deque

m, n = map(int,input().split())

box = [[] for _ in range(n)]

for i in range(n):
    box[i] = list(map(int,input().split()))

def ripened_tomato(queue,total):
    days = -1
    ripen = 0

    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    while(queue):
        days += 1
        for _ in range(len(queue)): 
            x,y= queue.popleft()
            ripen += 1
            for dx,dy in dir:
                x_,y_ = x+dx, y+dy
                if 0<=x_<m and 0<=y_<n and box[y_][x_]==0:
                    box[y_][x_] = 1
                    queue.append((x_,y_))
    
    if ripen != total:
        return -1
    
    return days

total = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((j,i))
        if box[i][j] != -1:
            total += 1

print(ripened_tomato(queue,total))