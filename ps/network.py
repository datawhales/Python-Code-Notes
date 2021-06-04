""" 네트워크.
    Link: https://programmers.co.kr/learn/courses/30/lessons/43162
"""
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(graph, i, visited)

def solution(n, computers):
    cnt = 0
    visited = [False] * n    
    for computer in range(n):
        # computer: 0
        # computers[computer]: [1, 1, 0]
        if visited[computer] == False:
            cnt += 1
            dfs(computers, computer, visited)
    return cnt

if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    answer = 2
    result = solution(n, computers)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """