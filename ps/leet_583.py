""" Leetcode. DP.
    583. Delete Operation for Two Strings
    Link: https://leetcode.com/problems/delete-operation-for-two-strings/
"""
from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                    
        return len(word1) + len(word2) - 2 * dp[-1][-1]

if __name__ == "__main__":
    word1 = "sea"
    word2 = "eat"
    answer = 2
    sol = Solution()
    result = sol.minDistance(word1, word2)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """