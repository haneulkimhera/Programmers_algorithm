n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(str,input().split())))

# for i in range(n):
#     print(graph[i])

home = (0,0)
school = (n-1,n-1)

def dfs(start):
    stack = [(0,0,start,"number")]
    x_dir = [1,0]
    y_dir = [0,1]
    sum_list = []
    while(stack):
        x,y,sum,step = stack.pop()
        # print(f"({x},{y}):{graph[y][x]}, sum:{sum}")
        if (x,y) == (n-1,n-1):
            sum_list.append(sum)
        for i in range(2):
            x_ = x+x_dir[i]
            y_ = y+y_dir[i]
            if (0<=x_<n) and (0<=y_<n):
                next = graph[y_][x_]
                if step == "number":
                    # print(f"({x_},{y_}):{graph[y_][x_]} ----> stack appended: {x_,y_,sum,next}")
                    stack.append((x_,y_,sum,next))
                else:
                    next = int(next)
                    if step=="+":
                        sum_ = sum + next
                    elif step=="-":
                        sum_ = sum - next
                    elif step=="*":
                        sum_ = sum * next
                    # print(f"({x_},{y_}):{graph[y_][x_]} ----> stack appended: {x_,y_,sum_,next}")
                    stack.append((x_,y_,sum_,"number"))
    return sum_list

sum_list = sorted(dfs(int(graph[0][0])))
print(sum_list[-1],sum_list[0])