from collections import deque
import copy

def solution(game_board, table):

    def find_pieces(table,indicator,d_indicator):
        n = len(table)
        m = len(table[0])
        
        def find_coordinates(x,y):
            coordinates = [(x,y)]
            stack = [(x,y)]
            table[y][x] = d_indicator
            x_dir = [1,-1,0,0]
            y_dir = [0,0,1,-1]
            while(stack):
                x,y = stack.pop()
                for i in range(4):
                    x_ = x+x_dir[i]
                    y_ = y+y_dir[i]
                    # print(f"\tx_:{x_}, y_:{y_}")
                    if (0<=x_<m and 0<=y_<n) and (table[y_][x_]==indicator):
                        # print(f"\t{table[y_][x_]} 해당")
                        table[y_][x_] = d_indicator
                        stack.append((x_,y_))
                        coordinates.append((x_,y_))
            coordinates.sort(key=lambda x:(x[1],x[0]))
            return coordinates
        
        def translate_coordinates(coordinates):
            h = max(coord[1] for coord in coordinates) - min(coord[1] for coord in coordinates)+1
            w = max(coord[0] for coord in coordinates) - min(coord[0] for coord in coordinates)+1
            n = len(coordinates)
            # print(f"min_y:{min(coord[1] for coord in coordinates)}, min_x:{min(coord[0] for coord in coordinates)}")
            piece = [[0]*(w) for _ in range(h)]
            for x,y in coordinates:
                # print(f"piece[y-min][x-min] = [{y-min(coord[1] for coord in coordinates)}][{x-min(coord[0] for coord in coordinates)}]")
                piece[y-min(coord[1] for coord in coordinates)][x-min(coord[0] for coord in coordinates)] = 1
            return n,(w,h),piece
        
        pieces = []
        for y in range(n):
            for x in range(m):
                if table[y][x] == indicator:
                    # coord = find_coordinates(x,y)
                    # print(f"-- find_coordinates --\n",coord)
                    # coord = translate_coordinates(coord)
                    # print(f"-- translate_coordinates --\n",coord)
                    pieces.append(translate_coordinates(find_coordinates(x,y)))

        return pieces
    
    def rotate(piece):
        n=piece[0]
        w,h = piece[1]
        coordinates = piece[2]
        rotated = [[0]*h for _ in range(w)]
        for y in range(h):
            for x in range(w):
                rotated[x][h-1-y] = coordinates[y][x]
        return n,(h,w),rotated
    
    pieces = find_pieces(table,1,0)
    blanks = find_pieces(game_board,0,1)

    # print("-- pieces --")
    # for piece in pieces:
    #         print(piece)

    # print("-- blanks --")
    # for blank in blanks:
    #         print(blank)

    answer = 0
    while(blanks):
        n, size_b, blank = blanks.pop()
        # print(f"<blank:{blank}>")
        for piece in pieces:
            # print(f"piece:{piece}")
            piece_org = copy.deepcopy(piece)
            found = False
            for _ in range(4):
                piece = rotate(piece)
                # print(f"\t{piece}")
                if blank == piece[2]:
                    answer+=n
                    pieces.remove(piece_org)
                    found = True
                    # print(f"!!match!! ------> answer:{answer}")
                    break
            if found:
                break

    # print(f"answer >>>> {answer}")
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])




