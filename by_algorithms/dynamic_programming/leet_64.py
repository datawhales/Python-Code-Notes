""" Leetcode. DP.
    64. Minimum Path Sum
    Link: https://leetcode.com/problems/minimum-path-sum/
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    continue
                if j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    answer = 7
    sol = Solution()
    result = sol.minPathSum(grid)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 7
    result: 7
    비교: True
    """