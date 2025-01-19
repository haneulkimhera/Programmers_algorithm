def solution():
    N, M = map(int,input().split())
    truth = list(map(int,input().split()))
    # print(truth)
    len_truth = truth.pop(0)
    parties = []

    parent = [-1]*(N+1)
    def find(x):
        if parent[x]<0:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]

    def union(x,y):
        x = find(x)
        y = find(y)
        if x==y:
            return
        else:
            if parent[x]<=parent[y]:
                if parent[x]==parent[y]:
                    parent[x] -= 1
                parent[y] = x
            else:
                parent[x] = y

    for person in truth:
        union(0,person)

    for _ in range(M):
        parties.append(list(map(int,input().split()))[1:])

    if len_truth==0:
        return M

    for attendants in parties:
        for i in range(len(attendants) - 1):
            union(attendants[i], attendants[i + 1])
    
    answer = 0
    for attendants in parties:
        if all(find(a) != find(0) for a in attendants):  # 진실 그룹과 연결되지 않은 경우
            answer += 1
            
    return answer

print(solution())