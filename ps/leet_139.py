""" Leetcode. DP.
    139. Word Break
    Link: https://leetcode.com/problems/word-break/
"""
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i+1] in set(wordDict):
                    dp[i+1] = True
                    break
        return dp[-1]
        
if __name__ == "__main__":
    s = 'leetcode'
    wordDict = ['leet', 'code']
    answer = True

    sol = Solution()
    result = sol.wordBreak(s, wordDict)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """