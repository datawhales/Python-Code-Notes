""" 여행경로.
    Link: https://programmers.co.kr/learn/courses/30/lessons/43164
"""
from collections import defaultdict

def solution(tickets):
    # {'ICN': ['ATL', 'SFO'], 
    # 'SFO': ['ATL'], 
    # 'ATL': ['ICN', 'SFO']}
    ret = []
    graph = defaultdict(list)
    for dep, arr in tickets:
        graph[dep].append(arr)
    for key in graph:
        graph[key].sort()

    def dfs(node, path):
        # 경로 추가되었으면 해당 경로를 반환
        if len(ret) == 1:
            return ret
        # 경로 완료 조건
        if len(path) == len(tickets) + 1:
            ret.append(path)
        for i, city in enumerate(graph[node]):
            graph[node].pop(i)
            dfs(city, path + [city])
            graph[node].insert(i, city)
    dfs('ICN', ['ICN'])
    return ret[0]
 
if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    answer = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    result = solution(tickets)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    result: ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    비교: True
    """