""" Leetcode. DFS.
    695. Max Area of Island
    Link: https://leetcode.com/problems/max-area-of-island/
"""
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            if grid[x][y] == 1:
                grid[x][y] = 0
                return 1 + dfs(x-1, y) + dfs(x, y-1) + dfs(x+1, y) + dfs(x, y+1)
        cnt = 0
        for i in range(m):
            for j in range(n):
                cnt = max(cnt, dfs(i, j))
        return cnt

if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    answer = 6
    sol = Solution()
    result = sol.maxAreaOfIsland(grid)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 6
    result: 6
    비교: True
    """