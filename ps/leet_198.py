""" Leetcode. DP.
    198. House Robber
    Link: https://leetcode.com/problems/house-robber/
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 예외 처리
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums))
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    answer = 12

    sol = Solution()
    result = sol.rob(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 12
    result: 12
    비교: True
    """