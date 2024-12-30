n = int(input())

height_map = []
rain = []
for i in range(n):
    row = input()
    height_map.append(list(map(int,row.split())))
    rain.append(sorted(list(map(int,row.split())),reverse=True)[0])

max_rain = sorted(rain,reverse=True)[0]

def draw_sink_map(height_map,rain):
    sink_map = [[1]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if height_map[y][x] <= rain:
                sink_map[y][x] = 0
    return sink_map

def dfs(x,y,sink_map):
    stack = [(x,y)]
    sink_map[y][x] = 0
    x_dir = [1,-1,0,0]
    y_dir = [0,0,1,-1]

    while(stack):
        x,y = stack.pop()
        for i in range(4):
            x_ = x+x_dir[i]
            y_ = y+y_dir[i]
            if (0<=x_<=n-1 and 0<=y_<=n-1) and (sink_map[y_][x_]==1):
                print(f"sinkmap({x_},{y_}): {sink_map[y_][x_]}")
                sink_map[y_][x_] = 0
                stack.append((x_,y_))

safe_regions = []
for i in range(max_rain):
    cnt = 0
    sink_map = draw_sink_map(height_map,i)
    print(sink_map)
    for y in range(n):
        for x in range(n):
            if sink_map[y][x] == 1:
                dfs(x,y,sink_map)
                cnt += 1
    safe_regions.append(cnt)

print(max(safe_regions))

