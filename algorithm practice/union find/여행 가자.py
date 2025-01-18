N = int(input())
M = int(input())

parent = [-1]*(N)
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
            parent[y] = x
        else:
            if parent[x]==parent[y]:
                parent[y] -= 1
            parent[x] = y

for i in range(N):
    link = list(map(int,input().split()))
    for j in range(N):
        if link[j] == 1:
            union(i,j)

dest = list(map(int,input().split()))

if all(find(dest[0]-1)==find(dest[i]-1) for i in range(M)):
    print("YES")
else:
    print("NO")