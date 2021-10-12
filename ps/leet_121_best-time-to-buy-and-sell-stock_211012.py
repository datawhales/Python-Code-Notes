""" Leetcode.
    121. Best Time to Buy and Sell Stock
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            if i == 0:
                min_price = prices[i]
            elif prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    answer = 5

    sol = Solution()
    result = sol.maxProfit(prices)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 5
    result: 5
    비교: True
    """