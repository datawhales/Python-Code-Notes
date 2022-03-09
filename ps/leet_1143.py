""" Leetcode. DP.
    1143. Longest Common Subsequence
    Link: https://leetcode.com/problems/longest-common-subsequence/
"""
from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[-1][-1]

if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    answer = 3
    sol = Solution()
    result = sol.longestCommonSubsequence(text1, text2)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """