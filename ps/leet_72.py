""" Leetcode. DP.
    72. Edit Distance
    Link: https://leetcode.com/problems/edit-distance/
"""
from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[i+j for i in range(n+1)] for j in range(m+1)]
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j] + 1, dp[i][j+1] + 1, dp[i+1][j] + 1)
        return dp[-1][-1]

if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    answer = 3
    sol = Solution()
    result = sol.minDistance(word1, word2)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """