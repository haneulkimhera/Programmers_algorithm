import collections

def solution(clothes):
    answer = 1

    if(len(clothes)==1):
        return answer
    
    clothes = list(map(lambda x:x[1], clothes))
    clothes = collections.Counter(clothes)
    clothes = sorted(clothes.items(), key= lambda x:x[1])
    print(clothes)

    num = len(clothes)

    for i in range(num):
        answer = answer*(clothes[i][1]+1)
    answer -= 1

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

'''
# 유형
<< 가능한 조합의 경우 >>

# 문제요구사항
- 의상목록에서 가능한 조합의 '개수' -> 어떤 조합인지는 알 필요 X

# 접근
- 의상목록의 종류 별 개수를 구하기
- 종류 별 개수를 이용해 가능한 조합 구하기
- 중복을 허용하지 않으므로, 가능한 모든 조합은 (모든 종류에 대해 (각 종류별 의상 개수(각 종류에서 의상 하나를 고르는 경우) + 1(선택하지 않는 경우))의 누적 곱) - 1(아무 종류의 옷도 안 입는 경우)
  
# 문제풀이
- 해시맵을 이용해 종류별 개수 딕셔너리 관리
- for문에서 누적곱, 마지막에 1 차감

************************** 핵심 **************************
- 종류 별 개수를 세야 함 => 해시맵 이용
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
각 종류에서 해당 종류를 안 입는 경우 1 더할 것 =
최소 1개 이상 착용해야 하므로 모든 조합의 경우에서 공집합의 경우 1 뺄 것
'''