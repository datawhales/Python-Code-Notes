""" Leetcode. DP.
    309. Best Time to Buy and Sell Stock with Cooldown
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 특수 조건 처리
        if len(prices) < 2:
            return 0
        free = 0
        hold, cooldown = float('-inf'), float('-inf')
        for i in range(len(prices)):
            free, hold, cooldown = max(free, cooldown), max(hold, free - prices[i]), hold + prices[i]
        return max(free, cooldown)

if __name__ == "__main__":
    prices = [1,2,3,0,2]
    answer = 3
    sol = Solution()
    result = sol.maxProfit(prices)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """