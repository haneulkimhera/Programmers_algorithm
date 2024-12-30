from collections import deque

def solution(maps):

    n = len(maps)
    m = len(maps[0])

    maps.insert(0,[0]*m)
    maps.append([0]*m)
    for i in range(n+2):
        maps[i].insert(0,0)
        maps[i].append(0)
    
    if(maps[n][m-1]==0 and maps[n-1][m]==0):
        return -1

    visited = [[0]*(m+2) for _ in range(n+2)]
    bfs = deque()
    answer = 0
    row_dir = [1,-1,0,0]
    col_dir = [0,0,1,-1]

    bfs.append([1,(1,1)])
    visited[1][1]=1

    while(bfs):
        cnt, loc = bfs.popleft()
        print(f"cnt:{cnt} loc:{loc}")

        if loc==(n,m):
            return cnt
        
        for i in range(4):
            row_ = loc[0]+row_dir[i]
            col_ = loc[1]+col_dir[i]
            print(f"row_:{row_} col_:{col_} -> {maps[row_][col_]} and {visited[row_][col_]}")

            if maps[row_][col_] == 1 and visited[row_][col_] == 0:
                bfs.append([cnt+1,(row_,col_)])
                visited[row_][col_] = 1
        
    return -1

print(solution([[1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 1]]))

'''
# 유형
<< 그래프 탐색 - 2차원 배열에서 최단거리 >>

# 문제요구사항
- 최단 거리의 "길이" -> 경로는 몰라도 됨, 길이만 중요

# 접근
- 격자형 2차원 그래프에서 이동 => 그래프 탐색( 노드(칸)와 간선(이동 가능 경로) )
- 모든 경로 아닌 "최단" 거리 => BFS (가장 먼저 도착한 경로가 최단 경로임을 보장!!)
- 필요한 정보 = 최단 경로의 "길이" -> bfs 트리의 노드에 현재 경로까지의 길이 저장
- 최단 거리 보장을 위해 이미 방문한 칸은 다시 방문하지 않아야!!

# 문제풀이
(1) BFS로 탐색
    - 상대 진영에 도달한 순간 현재 이동 횟수를 반환.
    - 다음 이동 가능 위치를 확인하여 큐에 추가.
(2) 방문 여부 체크
    - 이미 방문한 칸은 다시 방문하지 않도록 해야 함.
    - visited 배열을 사용하거나 maps를 갱신.
(3) 탐색 실패 시
    - BFS 종료 후 상대 진영에 도달하지 못하면 -1 반환.

************************** 핵심 **************************
2차원 배열을 주었고, 이동 가능 여부를 0과 1로 나누어 줌 => "격자형 그래프 탐색"
최단 거리 요구 => BFS, 방문여부관리
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
목표물의 바로 위,옆이 막힌 경우 말고도 목표물에 접근할 수 없는 경우 존재
 -> 바로 위/옆이 1인 경우만 -1을 반환하도록 하면 통과하지 못 함 => while(queue)를 빠져나올 때까지 정답을 못 찾으면 answer이 아닌 -1 반환하도록 해야함.
'''