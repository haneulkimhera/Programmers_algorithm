from collections import deque

def draw_map(rectangle):

    map = [[0]*102 for _ in range(102)]

    for x1,y1,x2,y2 in rectangle:
        x1 = x1*2
        x2 = x2*2
        y1 = y1*2
        y2 = y2*2

        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                if (x==x1 or x==x2 or y==y1 or y==y2):
                    if (map[y][x]==0):
                        map[y][x] = 1
                else:
                    map[y][x] = 2

        # print(x1,y1,x2,y2)
        # for i in range(101,-1,-1):
        #         print(map[i])

    for i in range(101,-1,-1):
        for j in range(102):
            if map[i][j] > 1:
                map[i][j] = 0
        # print(map[i])

    return map

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    characterX = characterX*2
    characterY = characterY*2
    itemX = itemX*2
    itemY = itemY*2

    map = draw_map(rectangle)

    bfs = deque()
    bfs.append((characterX,characterY,0))

    x_dir = [1,-1,0,0]
    y_dir = [0,0,1,-1]
    map[characterY][characterX] = 2
    visited = [[0]*102 for _ in range(102)]
    visited[characterY][characterX] = 1

    while(bfs):
        x,y,cnt = bfs.popleft()
        # print(x,y,cnt)
        if (x,y) == (itemX,itemY):
            return cnt//2
        for i in range(4):
            x_ = x + x_dir[i]
            y_ = y + y_dir[i]
            if x_<0 or y_<0:
                continue
            if map[y_][x_] == 1:
                bfs.append((x_,y_,cnt+1))
                map[y_][x_] = 2

    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))
'''
# 유형
<< >>

# 문제요구사항
- 

# 접근
- 

# 문제풀이

************************** 핵심 **************************
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!

'''