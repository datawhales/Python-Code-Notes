""" Leetcode.
    32. Longest Valid Parentheses
    Link: https://leetcode.com/problems/longest-valid-parentheses/
"""
from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
    
        dp = [0] * (len(s) + 1)
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    x = stack.pop()
                    dp[i+1] = dp[x] + i - x + 1
        
        return max(dp)

if __name__ == "__main__":
    s = ")()())"
    answer = 4
    sol = Solution()
    result = sol.longestValidParentheses(s)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 4
    result: 4
    비교: True
    """