from collections import deque

def solution(numbers, target):
    answer = 0

    bfs = deque()
    bfs.append((0,numbers[0]))
    bfs.append((0,numbers[0]*(-1)))

    while(bfs):
        idx, cur = bfs.popleft()

        if idx==len(numbers)-1:
            if cur==target:
                answer+=1
            continue

        bfs.append([idx+1, cur+numbers[idx+1]])
        bfs.append([idx+1, cur+(numbers[idx+1]*(-1))])

    return answer

print(solution([1,1,1,1,1],3))

'''
# 유형
<< 목표값 도달 방법 탐색 >>

# 문제요구사항
- 가능한 경우의 수를 모두 확인한 후 target을 만족하는 "경우의 수" -> 도달방법은 몰라도 됨. 방법의 총 개수만 알면 됨.

# 접근
- 순서를 바꾸지 않고 주어진 값들(numbers)을 대상으로 각 단계마다 두 가지 선택(더하기, 빼기)을 반복하면서 가능한 모든 조합을 시도해야함 -> "순열"의 문제
  => 완전탐색

# 문제풀이
- bfs 활용

************************** 핵심 **************************
- "순서를 바꾸지 않고" 각 단계에서 더하기or빼기를 했을 때 "target이 되는 경우의 수"를 구해야
  => 순열, 완전탐색
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
bfs=[] 으로 스택 만들어서 dfs.pop(0)하면 시간초과. deque()로 만들어야 시간초과 안 남
(재귀방식 dfs를 사용할 수 있지만 시간효율에서는 큰 차이 안 남. 어차피 둘 다 완전탐색, but 메모리효율에서는 차이 O)
'''