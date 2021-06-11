""" 단어 변환. BFS.
    Link: https://programmers.co.kr/learn/courses/30/lessons/43163
"""
from collections import deque

def check_diff(s1, s2):
    return sum([1 if s1[i] != s2[i] else 0 for i in range(len(s1))])

def bfs(graph, v, visited):
    queue = deque([v])
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x] + 1

def solution(begin, target, words):
    if target not in words:
        return 0
    words.append(begin)
    visited = [0] * len(words)
    graph = [[i for i in range(len(words)) if check_diff(words[i], words[j]) == 1] for j in range(len(words))]
    bfs(graph, len(words) - 1, visited)
    for i in range(len(words)):
        if target == words[i]:
            return visited[i]

if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    answer = 4
    result = solution(begin, target, words)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 4
    result: 4
    비교: True
    """