""" Leetcode. DP.
    62. Unique Paths
    Link: https://leetcode.com/problems/unique-paths/
"""
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                # print(f'i, j: {i}, {j}, dp[i][j]: {dp[i][j]}')
        return dp[-1][-1]

if __name__ == "__main__":
    m = 3
    n = 7
    answer = 28
    sol = Solution()
    result = sol.uniquePaths(m, n)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 28
    result: 28
    비교: True
    """