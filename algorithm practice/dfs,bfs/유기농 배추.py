def dfs(x,y):

    stack = [(x,y)]

    x_move = [1,-1,0,0]
    y_move = [0,0,1,-1]

    while(stack):
        x,y = stack.pop()

        for i in range(4):
            x_ = x+x_move[i]
            y_ = y+y_move[i]
            
            if (x_>=0 and y_>=0) and (graph[y_][x_]==1):
                graph[y_][x_] = 0
                stack.append((x_,y_))

t = int(input())

for i in range(t):
    m,n,k = map(int,input().split())
    graph = [[0]*(m+1) for i in range(n+1)]

    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1

    network = 0


    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                dfs(j,i)
                network+=1

    print(network)