m,n,k = map(int, input().split())
graph = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            graph[y][x] = 1

def dfs(x,y):
    stack = [(x,y)]
    graph[y][x] = 1
    x_dir = [1,-1,0,0]
    y_dir = [0,0,1,-1]
    area = 1

    while(stack):
        x,y = stack.pop()
        for i in range(4):
            x_ = x+x_dir[i]
            y_ = y+y_dir[i]
            if (0<=x_<n and 0<=y_<m) and graph[y_][x_]==0:
                graph[y_][x_] = 1
                area += 1
                stack.append((x_,y_))

    return area

total = 0
areas = []
for y in range(m):
    for x in range(n):
        if graph[y][x]==0:
            areas.append(dfs(x,y))
            total+=1

areas = sorted(areas)
each = ""
for area in areas:
    each = each + str(area) + " "
    
print(total)
print(each)
