""" Leetcode. DP.
    91. Decode Ways
    Link: https://leetcode.com/problems/decode-ways/
"""
from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        # 예외 처리
        if not s:
            return 0
        dp = [0] * len(s)
        dp[0] = 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            if i == 1:
                if 0 < int(s[1]) <= 9:
                    dp[1] += dp[0]
                if 10 <= int(s[0:2]) <= 26:
                    dp[1] += dp[0]
                continue
            if 0 < int(s[i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

if __name__ == "__main__":
    s = "226"
    answer = 3
    sol = Solution()
    result = sol.numDecodings(s)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """