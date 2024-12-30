n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):

    cnt = 1
    stack = [(x,y)]
    graph[y][x] = 0
    x_dir = [1,-1,0,0]
    y_dir = [0,0,1,-1]

    while(stack):
        x,y = stack.pop()
        for i in range(4):
            x_ = x+x_dir[i]
            y_ = y+y_dir[i]
            if (0<=x_<=n-1 and 0<=y_<=n-1) and (graph[y_][x_]==1):
                graph[y_][x_] = 0
                cnt += 1
                stack.append((x_,y_))

    return cnt

list = []

for y in range(n):
    for x in range(n):
        if graph[y][x]==1:
            cnt = dfs(x,y)
            list.append(cnt)

list = sorted(list)

print(len(list))
for i in list:
    print(i)


