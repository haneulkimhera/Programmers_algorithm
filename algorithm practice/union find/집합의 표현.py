n, m = map(int,input().split())

parent = [-1]*(n+1)

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
        if parent[x]<parent[y]:
            parent[x]+=parent[y]
            parent[y] = x
        else:
            parent[y]+=parent[x]
            parent[x] = y


answer = []
for i in range(m):
    operator,x,y = map(int,input().split())
    if operator == 0:
        union(x,y)
    elif operator == 1:
        answer.append("YES" if find(x)==find(y) else "NO")

for a in answer:
    print(a)