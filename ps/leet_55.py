""" Leetcode. DP.
    55. Jump Game
    Link: https://leetcode.com/problems/jump-game/
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        for idx in range(len(nums) - 2, -1, -1):
            if idx + nums[idx] >= end:
                end = idx
        return end == 0

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    answer = True
    sol = Solution()
    result = sol.canJump(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """