from collections import deque
m,n,h = map(int,input().split())
box = [[[] for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        box[i][j] = list(map(int,input().split()))

# print(box[0])
# print(box[0][0])
# print(box[0][0][0])

total = 0
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            # print(f"box[{i}][{j}][{k}]")
            if box[i][j][k]==1:
                queue.append((k,j,i))
                # print(f"appended -> {k},{j},{i}")
            if box[i][j][k]!=-1:
                total += 1

# print(f"queue: {queue}")
def ripened_tomatoes(queue,total):
    ripen = len(queue)
    days = -1
    direction = [(-1,0,0),(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

    while(queue):
        days += 1
        # print(f">>>>>> days: {days}")
        # print("---------------------")
        # for i in range(h):
        #     for j in range(n):
        #         print(box[i][j])
        #     print()
        # print("---------------------")
        for _ in range(len(queue)):
            x,y,z = queue.popleft()
            for dz,dx,dy in direction:
                x_, y_, z_ = x+dx, y+dy, z+dz
                # print(f"x_:{x_}, y_:{y_}, z_:{z_}")
                if (0<=z_<h and 0<=x_<m and 0<=y_<n) and box[z_][y_][x_]==0:
                    box[z_][y_][x_] = 1
                    # print(f"box[{z_}][{y_}][{x_}] = 1")
                    ripen += 1
                    queue.append((x_,y_,z_))
    
    if ripen == total:
        return days
    
    return -1

print(ripened_tomatoes(queue,total))