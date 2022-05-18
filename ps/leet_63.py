""" Leetcode. DP.
    63. Unique Paths II
    Link: https://leetcode.com/problems/unique-paths-ii/
"""
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        return dp[-1][-1]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    answer = 2
    sol = Solution()
    result = sol.uniquePathsWithObstacles(obstacleGrid)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """