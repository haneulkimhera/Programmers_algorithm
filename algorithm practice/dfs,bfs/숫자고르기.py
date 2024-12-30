n = int(input())
# print(f"n:{n}")

numbers = [0]*(n+1)

for i in range(n):
    number = int(input())
    # print(f"number:{number}")
    numbers[i+1]=number

visited = [0]*(n+1)

def dfs(start):
    # print(f"dfs started. dfs({start})>>>")
    stack=[start]
    cnt = 1
    nums = [start]
    while(stack):
        top = stack.pop()
        bottom = numbers[top]
        if bottom == start:
            return cnt, nums
        if visited[bottom]==0 and bottom not in nums:
            stack.append(bottom)
            nums.append(bottom)
            cnt += 1
    return 0,[]

total = 0
answer = []
for i in range(1,n+1):
    if visited[i]==0:
        cnt,nums = dfs(i)
        total += cnt
        for num in nums:
            visited[num]=1
            answer.append(num)
            
print(total)
answer = sorted(answer)

for i in answer:
    print(i)

# 1234567
# 2345671
# 3514267