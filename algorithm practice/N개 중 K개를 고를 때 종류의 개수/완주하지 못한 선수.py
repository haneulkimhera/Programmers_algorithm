def solution(participant, completion):
    num = len(completion)

    if num == 1:
        return participant[0]
    
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(num):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[num]

'''
# 유형
<< N개의 아이템 중 누락된 아이템 구하기 >>

# 문제요구사항
- 완주하지 못한 선수의 "이름"

# 접근
- 동명이인이 존재하기 때문에 단순히 고유원소로는 해결할 수 없음 !!
- 두 리스트를 직접 1:1 비교하여 다른 원소를 찾아야함
  
# 문제풀이
- 리스트를 이름순으로 정렬, 비교하여 다른 이름이 나타나는 지점을 찾음

************************** 핵심 **************************
동명이인이 존재하기 때문에 단순히 고유원소로는 해결할 수 없음!
1:1 비교해야하며 "이름"을 반환해야 하기 때문에 이름을 유지해야함
성능을 위해 이름순으로 정렬 후 비교
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
참가자가 1명인 경우 len(completion)이 0이기 때문에 반복문에서 completion[i] 에러 발생.
=> 참가자가 1인 경우 미리 체크해 에러방지 해야함
'''