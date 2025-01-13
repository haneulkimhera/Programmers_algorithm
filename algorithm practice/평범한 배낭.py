from collections import deque

n,k = map(int,input().split())
items = []
for i in range(n):
    w,v = map(int,input().split())
    items.append((w,v))

acc = [0]*(k+1)

for w,v in items:
    for cur in range(k,w-1,-1):
        acc[cur] = max(acc[cur],acc[cur-w]+v)

print(acc[k])
