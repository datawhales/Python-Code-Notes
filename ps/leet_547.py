""" Leetcode.
    547. Number of Provinces
    Link: https://leetcode.com/problems/number-of-provinces/
"""
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        def dfs(graph, visited, x):
            if not visited[x]:
                # 방문 처리
                visited[x] = True
                for i in range(len(graph[x])):
                    if graph[x][i] == 1:
                        dfs(graph, visited, i)
                return True
            return False
        cnt = 0
        for i in range(len(isConnected)):
            if dfs(isConnected, visited, i):
                cnt += 1
        return cnt

if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    answer = 2
    sol = Solution()
    result = sol.findCircleNum(isConnected)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """