""" Leetcode.
    121. Best Time to Buy and Sell Stock
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 한 번 순회하는 동안 현재까지 지나온 지점 중 최소 지점을 저장하고,
            현재 위치의 가격 - 최소 가격이 현재까지 중의 가장 큰 이익보다 크면 이를 가장 큰 이익에 저장하는 방식.
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
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