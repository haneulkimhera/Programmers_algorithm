from collections import defaultdict

def solution():
    n = int(input())
    id_map = {}
    parent = {}
    rate = {}
    answers = []

    def find(x):
        if parent[x] == x:
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
            if rate[x]>rate[y]:
                parent[y] = x
                rate[x] += rate[y]
            else:
                parent[x] = y
                rate[y] += rate[x]

    id = 0
    for i in range(n):
        answer = 0
        x,y = map(str,input().split())
        if x not in id_map:
            id_map[x] = id
            parent[id] = id
            rate[id] = 1
            id += 1
        if y not in id_map:
            id_map[y] = id
            parent[id] = id
            rate[id] = 1
            id += 1

        union(id_map[x],id_map[y])
        answers.append(rate[find(id_map[x])])
    
    return answers

n = int(input())
answers = []
for i in range(n):
    answers += solution()

for answer in answers:
    print(answer)
