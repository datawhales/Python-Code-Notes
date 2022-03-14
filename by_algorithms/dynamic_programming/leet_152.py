""" Leetcode. DP.
    152. Maximum Product Subarray
    Link: https://leetcode.com/problems/maximum-product-subarray/
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 예외 처리
        if len(nums) < 2:
            return nums[0]
        dp_min, dp_max = nums[0], nums[0]
        ret = nums[0]
        for i in range(1, len(nums)):
            dp_min, dp_max = min(nums[i], dp_min * nums[i], dp_max * nums[i]), max(nums[i], dp_max * nums[i], dp_min * nums[i])
            ret = max(dp_max, ret)
        return ret

if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    answer = 6
    sol = Solution()
    result = sol.maxProduct(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 6
    result: 6
    비교: True
    """