N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

def print_board():
    for i in range(N):
        print(board[i])

def solution(board):

    tetrominos = [
        [[1,1,1,1]],
        [[1,1],[1,1]],
        [[1,0],[1,0],[1,1]],
        [[0,1],[0,1],[1,1]],
        [[1,0],[1,1],[0,1]],
        [[0,1],[1,1],[1,0]],
        [[1,1,1],[0,1,0]]
    ]

    def rotate(tetromino):
        # print(f"<{tetromino}>")
        n = len(tetromino)
        m = len(tetromino[0])
        rotated = [[0]*n for _ in range(m)]

        for y in range(n):
            for x in range(m):
                # print(f"roated[{x}][{n-1-y}] = tetromino[{y}][{x}]")
                rotated[x][n-1-y] = tetromino[y][x]

        return rotated
    
    total = []

    # 테트로미노 한 조각
    for tetromino in tetrominos:

        # 회전 한 번씩
        for _ in range(4):
            tetromino = rotate(tetromino)
            n = len(tetromino)
            m = len(tetromino[0])

            for board_y in range(N-n+1):
                for board_x in range(M-m+1):

                    sum = 0

                    for i in range(n):
                        for j in range(m):
                            cur_y = board_y + i
                            cur_x = board_x + j

                            if tetromino[i][j] == 1:
                                sum += board[cur_y][cur_x]

                    total.append(sum)

    return total

total = solution(board)
total = sorted(total,reverse=True)
print(total[0])