""" Leetcode. DP.
    322. Coin Change
    Link: https://leetcode.com/problems/coin-change/
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [-1] * 10001
        dp[0] = 0
        for i in range(1, amount+1):
            check_list = [dp[i-c] for c in coins if i-c >= 0 and dp[i-c] != -1]
            if not check_list:
                continue
            dp[i] = min(check_list) + 1
        return dp[amount]

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    answer = 3

    sol = Solution()
    result = sol.coinChange(coins, amount)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """