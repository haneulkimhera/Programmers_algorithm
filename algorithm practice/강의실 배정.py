import heapq

N = int(input())
lectures = []

for _ in range(N):
    s,t = map(int,input().split())
    lectures.append((s,t))

lectures.sort()
heap = []

for s, t in lectures:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, t)

print(len(heap))