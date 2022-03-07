""" Leetcode. DP.
    413. Arithmetic Slices
    Link: https://leetcode.com/problems/arithmetic-slices/
"""
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 예외 처리
        if len(nums) < 3:
            return 0
        dp = [0] * (len(nums) + 1)
        # dp = [0, 0, 0, 1, 1+2, 1+2+3, ..]
        for i in range(3, len(nums) + 1):
            dp[i] = dp[i-1] + i - 2
        diff = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]      
        ret = 0
        # sliding window
        left, right = 0, 0
        while left <= right and right < len(diff):
            if diff[left] == diff[right]:
                right += 1
            else:
                if right - left >= 2:
                    ret += dp[right - left + 1]
                left = right
                right += 1
        if right - left >= 2:
            ret += dp[right - left + 1]
        return ret

    def numberOfArithmeticSlices_2(self, nums: List[int]) -> int:
        ret = 0
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = dp[i-1] + 1
                ret += dp[i]
        return ret

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    answer = 3
    sol = Solution()
    result = sol.numberOfArithmeticSlices(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """