""" Leetcode.
    797. All Paths From Source to Target
    Link: https://leetcode.com/problems/all-paths-from-source-to-target/
"""
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        def dfs(visited):
            # 종료 조건
            if visited[-1] == len(graph) - 1:
                ret.append(visited)
                return
            # 현재까지의 경로를 담아 재호출
            for child in graph[visited[-1]]:
                dfs(visited + [child])
        dfs([0])
        return ret

if __name__ == "__main__":
    graph = [[1,2],[3],[3],[]]
    answer = [[0,1,3],[0,2,3]]
    sol = Solution()
    result = sol.allPathsSourceTarget(graph)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[0,1,3],[0,2,3]]
    result: [[0,1,3],[0,2,3]]
    비교: True
    """