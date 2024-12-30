def solution(n, s):
    quotient = s // n
    remainder = s % n

    if quotient == 0:
        return [-1]

    result = [quotient] * (n - remainder) + [quotient + 1] * remainder

    return result

solution(2,9)

'''
# 유형

# 문제요구사항

# 접근

# 문제풀이

************************** 핵심 **************************

**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
'''