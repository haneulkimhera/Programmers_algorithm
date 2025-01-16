N = int(input())
sea = []
shark = (0,0)
shark_size = 2
sec = -1

for i in range(N):
    sea.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if sea[i][j]==9:
            shark = (i,j)

def solution():
    def check_available(shark_size):
        fishes = []
        for i in range(N):
            for j in range(N):
                if sea[i][j] < shark_size:
                    fishes.append((i,j))
        return fishes

    move = [(1,0),(-1,0),(0,1),(0,-1)]

    while():
        shark_full = 0
        while(shark_full<shark_size):
            fishes = check_available(shark_size)
            
    return 0
        