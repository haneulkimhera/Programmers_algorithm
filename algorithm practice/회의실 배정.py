from collections import defaultdict

N = int(input())
meetings = []

for i in range(N):
    start, end = map(int,input().split())
    meetings.append((start,end))

meetings.sort(key=lambda x:(x[1],x[0]))

print(meetings)

pointer_s = 0
pointer_e = 0
cnt = 0

for meeting in meetings:
    start,end = meeting
    if end == pointer_e and start>pointer_e:
        print(f"{meeting} --> pass")
        continue
    if start>=pointer_e:
        pointer_e = end
        pointer_s = start
        print(f"{meeting} >>>> selected! s:{pointer_s} e:{pointer_e}")
        cnt += 1

print(cnt)

'''
0: 1(1)
1: 15(14)
2: 8(6)
3: 6(3)
4: 4(0) 6(2)
5: 6(1)
6: 6(0) 
7: 8(1)
'''