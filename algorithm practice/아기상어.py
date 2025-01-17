from collections import deque

def solution():
    N = int(input())

    # 바다맵
    sea = []
    for i in range(N):
        sea.append(list(map(int,input().split())))

    # 상어 위치
    shark = (0,0)
    for i in range(N):
        for j in range(N):
            if sea[i][j]==9:
                shark = (i,j)

    # 가장 가까운 물고기 위치, 걸리는 시간 조회 -> 없으면 -1 반환
    def closest_fish(shark_loc,shark_size):
        i,j = shark_loc
        queue = deque()
        visited = [[0]*N for _ in range(N)]

        move = [(-1,0),(0,-1),(0,1),(1,0)]
        queue.append((i,j,0))
        visited[i][j] = 1

        fishes = []
        thresh = 400

        while(queue):
            i,j,sec = queue.popleft()

            if sec>thresh:
                break
            
            if 0<sea[i][j]<shark_size:
                thresh = sec
                fishes.append((i,j))
            
            for di,dj in move:
                i_ = i+di
                j_ = j+dj
                if (0<=i_<N and 0<=j_<N) and (visited[i_][j_]==0) and (sea[i_][j_]<=shark_size):
                    # print(f"{(i_,j_,sec+1)}")
                    visited[i_][j_] = 1
                    queue.append((i_,j_,sec+1))
                    # print(queue)
        if len(fishes)==0:
            return -1
        
        fishes = sorted(fishes,key=lambda x:(x[0],x[1]))
        return fishes[0],thresh
        
    # 물고기 잡아먹는 것 처리
    def catch_fish(target_loc,shark_loc,eaten):
        target_y,target_x = target_loc
        shark_y,shark_x = shark_loc

        sea[target_y][target_x] = 9
        sea[shark_y][shark_x] = 0

        return target_loc,eaten+1

    # 시작
    shark_size = 2
    shark_loc = shark
    eaten = 0
    t = 0

    while(closest_fish(shark_loc,shark_size)!=-1):
        # print(f"\n***** 타겟 조회 - shark_loc:{shark_loc}, shark_size:{shark_size}")
        target_loc,dist = closest_fish(shark_loc,shark_size)
        shark_loc,eaten = catch_fish(target_loc,shark_loc,eaten)
        # print(f"target_fish:{target_loc}, distance:{dist}, eaten:{eaten}")

        if eaten == shark_size:
            shark_size += 1
            eaten = 0
            # print(f"!!! baby shark grown up >>> {shark_size}!!!")

        # for i in range(N):
        #     print(sea[i])

        t += dist
        # print(f"- - - - -time elapsed:{t} - - - - -")
    
    # print(f"먹을 수 있는 물고기 없음. t = {t}")
    return t

print(solution())