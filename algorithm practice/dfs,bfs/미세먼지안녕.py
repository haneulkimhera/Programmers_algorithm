from collections import deque

def solution():

    R,C,T = map(int,input().split())

    board = [[] for _ in range(R)]
    air_purifier = []

    for i in range(R):
        board[i] = list(map(int,input().split()))

    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                air_purifier.append((i,j))

    def diffusion():
        # t시점 시작에 먼지가 있는 곳 queue에 추가
        queue = deque()
        for i in range(R):
            for j in range(C):
                if board[i][j]>0 and board[i][j]!=-1:
                    queue.append((i,j))

        # t시점 시작에 가지고 있던 먼지로 계산한 확산될 먼지의 양
        dust_to_diffuse = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                dust_to_diffuse[i][j] = board[i][j]//5
        
        # 1초동안 t시점 시작에 먼지가 있던 곳 모두 확산 진행
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        for _ in range(len(queue)):
            r,c = queue.popleft()
            diffused_cnt = 0
            dust = dust_to_diffuse[r][c]
            for dr,dc in d:
                r_ = r+dr
                c_ = c+dc
                if (0<=r_<R and 0<=c_<C) and (board[r_][c_]!=-1):
                    board[r_][c_] += dust
                    diffused_cnt += 1
            board[r][c] -= dust*diffused_cnt

    def circulation_top(r,c):
        h=r+1
        w=c

        top = board[0]
        bottom = board[h-1][::-1]
        left = [board[i][0] for i in range(h-2,0,-1)]
        right = [board[i][w-1] for i in range(1,h-1,1)]

        outlines = top+right+bottom+left
        outlines = outlines[1:]+outlines[:1]

        board[0] = outlines[:w]
        for i in range(1,h-1,1):
            board[i][w-1] = outlines[w+i-1]
        board[h-1] = outlines[w+h-2:w+h-2+w][::-1]
        for i in range(1,h-1,1):
            board[i][0] = outlines.pop()
        
        board[h-1][0] = -1
        board[h-1][1] = 0

    def circulation_bottom(r,c):
        h=R-r
        w=c

        top = board[r]
        bottom = board[R-1][::-1]
        left = [board[i][0] for i in range(R-2,r,-1)]
        right = [board[i][w-1] for i in range(r+1,R-1,1)]

        outlines = top+right+bottom+left
        outlines = outlines[-1:]+outlines[:-1]

        board[r] = outlines[:w]
        for i in range(r+1,R-1,1):
            board[i][w-1] = outlines[w+i-r-1]
        board[R-1] = outlines[w+h-2:w+h-2+w][::-1]
        for i in range(r+1,R-1,1):
            board[i][0] = outlines.pop()
        
        board[r][0] = -1
        board[r][1] = 0
    
    def count_dust():
        total = 0

        for i in range(R):
            for j in range(C):
                if board[i][j] != -1:
                    total += board[i][j]
        
        return total
    
    top_r, top_c = air_purifier[0]
    sec = 0
    while(sec<T):
        sec += 1

        diffusion()
        # print(f"----diffusion----")
        # for i in range(R):
        #     print(board[i])

        circulation_top(top_r,C)
        circulation_bottom(top_r+1,C)
        # print(f"---circulation---")
        # for i in range(R):
        #     print(board[i])

    dust_total = count_dust()
    # print(f"------total------")
    print(dust_total)

solution()