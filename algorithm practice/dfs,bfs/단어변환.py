from collections import deque

def solution(begin, target, words):

    n = len(words)

    visited = [0]*n

    bfs = deque()
    bfs.append([0,begin])

    def countdiff(cur,next):
        diff = 0
        for i in range(len(cur)):
            if cur[i]!=next[i]:
                diff += 1
        return diff

    while(bfs):
        cnt,cur = bfs.popleft()

        if cur == target:
            return cnt

        for i in range(n):
            if not visited[i]:
                next = words[i]
                if countdiff(cur,next) == 1:
                    bfs.append([cnt+1,next])
                    visited[i] = 1
    
    return 0

'''
# 유형
<< >>

# 문제요구사항
- 

# 접근
- 

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
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
'''