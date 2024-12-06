def solution(phone_book):
    answer = True

    if len(phone_book) == 1:
        return answer

    phone_book = sorted(phone_book, key=lambda x: (x, len(x)))

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return answer

'''
# 유형
<< 배열에서 접두어 찾기 >>

# 문제요구사항
- 전화번호 목록에서 어떤 번호가 다른 번호의 접두어인 경우가 있는지 "여부"를 확인 -> 어떤 번호인지는 필요 없음

# 접근
- 정렬을 하면 접두어 관계가 인접한 번호들 사이에서만 발생하기 때문에, 한 번만 비교하면 됨
- 요소를 기준으로 정렬 후, 요소의 길이를 기준으로 오름차순으로 정렬 <- 그래야 해당 요소가 뒷 요소의 접두어인지 확인 가능
  
# 문제풀이
- 리스트를 정렬, startswith 사용

************************** 핵심 **************************
- 정렬 후 비교
- startswith() 메소드
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
전화번호가 1개인 경우 무조건 접두어 없음.
for문에서 에러 발생하기 때문에 사전에 예외처리.
'''