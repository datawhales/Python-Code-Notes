""" Leetcode. DP.
    139. Word Break
    Link: https://leetcode.com/problems/word-break/
"""
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            s = s.split(word)
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