def solution(s):
    answer = ""

    nums = sorted(s.split(" "), key = lambda x:int(x))
    print(nums)

    return nums[0]+" "+nums[-1]


solution("-1 -2 -3 -4")

'''
# 유형

# 문제요구사항

# 접근
큰 수일 수록 1번이라도 적게 더해지려면 작은 수랑 곱해져야
누적 차이를 줄이려면 한 쪽의 가장 작은 수와 다른 쪽의 가장 큰 수를 곱해야함

# 문제풀이

************************** 핵심 **************************

**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
'''