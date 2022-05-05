""" Leetcode. Backtracking.
    207. Course Schedule
    Link: https://leetcode.com/problems/course-schedule/
"""
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced, visited = set(), set()
        
        def dfs(i):
            if i in traced:
                return False
            
            if i in visited:
                return True
            
            traced.add(i)
            
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            traced.remove(i)
            visited.add(i)
            
            return True
    
        for x in list(graph):
            if not dfs(x):
                return False
    
        return True
    
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    answer = False
    sol = Solution()
    result = sol.canFinish(numCourses, prerequisites)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: False
    result: False
    비교: True
    """