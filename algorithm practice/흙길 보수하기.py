import math

N, L = map(int,input().split())
puddles = []
for _ in range(N):
    start, end = map(int,input().split())
    puddles.append([start,end])

puddles.sort(key=lambda x:x[1])
first_puddle = puddles[0]

pointer = 0
plank = 0

for puddle in puddles:
    start, end = puddle
    pointer = max(pointer,start)
    # print(f"puddle = ({start},{end}), standing at [{pointer}]")
    length = end-pointer
    needed = math.ceil(length/L)
    plank += needed
    pointer += (L*needed)
    # print(f">> plank: +{needed}, pointer:{pointer}")
    
print(plank)