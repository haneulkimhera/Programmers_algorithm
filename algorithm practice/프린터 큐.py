from collections import deque
def solution():

    N, M = map(int,input().split())
    rates = list(map(int,input().split()))
    docs = []
    for idx,rate in enumerate(rates):
        docs.append([idx,rate])
    docs = deque(docs)

    turn = 1
    pointer = 0
    while(True):
        cur_idx, cur_rate = docs.popleft()

        if cur_rate == max(rates):
            if cur_idx == M:
                return turn
            rates.remove(cur_rate)
            turn += 1
        else:
            docs.append([cur_idx, cur_rate])

test = int(input())
answers = []
for _ in range(test):
    answers.append(solution())

for i in range(test):
    print(answers[i])
