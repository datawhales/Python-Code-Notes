""" Leetcode.
    45. Jump Game II
    Link: https://leetcode.com/problems/jump-game-ii/
"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        left, right = 0, nums[0]
        ret = 1
        while right < len(nums)-1:
            ret += 1
            max_step = max(i + nums[i] for i in range(left, right+1))
            left, right = right, max_step
        return ret

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    answer = 2
    sol = Solution()
    result = sol.jump(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """