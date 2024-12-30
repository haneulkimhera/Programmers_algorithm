n = int(input())

painting_org = []
painting_rg = []
for i in range(n):
    row = input()
    painting_org.append(list(row))
    painting_rg.append(list(row))

for i in range(n):
    for j in range(n):
        if painting_rg[i][j]=="G":
            painting_rg[i][j] = "R"

def painting_bin(painting,color):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if painting[i][j]==color:
                result[i][j] = 1
    return result

def dfs(x,y,painting):
    stack = [(x,y)]
    painting[y][x] = 0
    x_dir = [1,-1,0,0]
    y_dir = [0,0,1,-1]
    while(stack):
        x,y = stack.pop()
        for i in range(4):
            x_ = x+x_dir[i]
            y_ = y+y_dir[i]
            if (0<=x_<n and 0<=y_<n) and painting[y_][x_] == 1:
                painting[y_][x_] = 0
                stack.append((x_,y_))

def find_area(painting_base, color):
    area = 0
    painting = painting_bin(painting_base,color)
    for y in range(n):
        for x in range(n):
            if painting[y][x] == 1:
                dfs(x,y,painting)
                area += 1
    return area

norm = 0
rg = 0
norm += find_area(painting_org,"R")
norm += find_area(painting_org,"G")
norm += find_area(painting_org,"B")
rg += find_area(painting_rg,"R")
rg += find_area(painting_rg,"B")

print(str(norm)+" "+str(rg))