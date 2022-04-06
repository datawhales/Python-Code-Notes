""" Leetcode. Sliding Window.
    209. Minimum Size Subarray Sum
    Link: https://leetcode.com/problems/minimum-size-subarray-sum/
"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        tmp = 0
        ret = len(nums) + 1
        for right, n in enumerate(nums):
            tmp += n
            while tmp >= target:
                ret = min(ret, right - left + 1)
                tmp -= nums[left]
                left += 1
        return ret if ret <= len(nums) else 0

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    answer = 2
    sol = Solution()
    result = sol.minSubArrayLen(target, nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """