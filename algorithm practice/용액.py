N = int(input())
solution = list(map(int,input().split()))

def search():
    start = 0
    end = N-1
    min_balance = 1000000001
    result = (0,0)
    while(start<end):
        balance = solution[start] + solution[end]

        if abs(balance) < abs(min_balance):
            min_balance = abs(balance)
            result = (start,end)
        
        if balance<0:
            start += 1
        elif balance>0:
            end -= 1
        else:
            break
    
    return result

x,y = search()

print(solution[x],solution[y])
