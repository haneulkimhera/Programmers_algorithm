from collections import defaultdict

def solution(tickets):
    route = []
    tickets = sorted(tickets, key=lambda x:x[1], reverse=True)

    graph = defaultdict(list)

    for dep,arr in tickets:
        graph[dep].append(arr)

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        route.append(airport)

    dfs("ICN")
    return route[::-1]

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

'''
# 유형
<< 그래프에서의 순열 문제 >>

# 문제요구사항
- "모든 티켓"을 사용하는 "경로"를 반환

# 접근
- 

# 문제풀이
(1) DFS

************************** 핵심 **************************
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
'''