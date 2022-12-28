""" Leetcode.
    53. Maximum Subarray
    Link: https://leetcode.com/problems/maximum-subarray/description/
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float("-inf")
        tmp_max = 0
        for n in nums:
            tmp_max = max(tmp_max + n, n)
            global_max = max(tmp_max, global_max)
        return global_max


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    answer = 6
    sol = Solution()
    result = sol.maxSubArray(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 6
    result: 6
    비교: True
    """
