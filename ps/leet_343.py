""" Leetcode. DP.
    343. Integer Break
    Link: https://leetcode.com/problems/integer-break/
"""
from typing import List

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        # n >= 4
        dp = [0] * (n+1)
        dp[1], dp[2], dp[3] = 1, 2, 3
        for i in range(4, n+1):
            dp[i] = max(2 * dp[i-2], 3 * dp[i-3])
        return dp[n]

if __name__ == "__main__":
    n = 10
    answer = 36
    sol = Solution()
    result = sol.integerBreak(n)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 36
    result: 36
    비교: True
    """