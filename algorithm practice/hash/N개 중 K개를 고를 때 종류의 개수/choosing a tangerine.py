import collections

def solution(k, tangerine):

    answer = 0

    # count = {}
    # for tan in tangerine:
    #     if tan in count:
    #         count[tan] +=1
    #     else:
    #         count[tan] = 1

    count = collections.Counter(tangerine)
    count = sorted(count.values(), reverse=True)

    picked = 0
    answer = 0
    
    for type_cnt in count:
        picked += type_cnt
        answer += 1

        if picked >= k : 
            return answer

    return answer

'''
# 유형
<< N개의 아이템 중 K개를 고를 때 최소 종류의 개수를 구하기 >>

# 문제요구사항
- 최대 K개의 귤 중 선택 가능한 가장 적은 "종류의 수"

# 접근
- 가장 많은 개수의 종류로 채우는 게 유리
- 개수별로 줄 세워 가장 많은 종류부터 채워나가기
  
# 문제풀이
- collections.counter 이용

************************** 핵심 **************************
가장 "적은 종류"의 개수를 찾는 게 목표 => 종류별 개수를 관리할 필요 O
---------------------------------------------------------------

- 원하는 것이 가장 "획일적인" 종류의 수 => 가장 많은 개수인 종류부터 "차례대로 채워나가야" 함

- 가능한 한 적은 종류의 수 = 가장 많은 개수인 종류부터 채워나가 최소한의 종류로 K개를 채워야함
  (그래서 원소별 개수를 세어야 함.
   어떤 종류가 가장 많은 개수를 가지는지가 중요.

**********************************************************
'''

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))