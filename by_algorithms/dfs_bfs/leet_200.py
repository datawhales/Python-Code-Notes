""" Leetcode.
    200. Number of Islands
    Link: https://leetcode.com/problems/number-of-islands/
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs_x_y(grid, x, y):
            # 종료 조건
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return False
            if grid[x][y] == "1":
                # 방문 처리
                grid[x][y] = "0"
                # 다음 위치 이동
                dfs_x_y(grid, x+1, y)
                dfs_x_y(grid, x, y+1)
                dfs_x_y(grid, x-1, y)
                dfs_x_y(grid, x, y-1)
                return True
            return False
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs_x_y(grid, i, j):
                    cnt += 1
        return cnt

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    answer = 1
    sol = Solution()
    result = sol.numIslands(grid)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 1
    result: 1
    비교: True
    """