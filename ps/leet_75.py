""" Leetcode.
    75. Sort Colors
    Link: https://leetcode.com/problems/sort-colors/
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        left, right = 0, len(nums)
        # left는 0일때만 이동
        # right는 2일때만 왼쪽으로 이동
        while cur < right:
            if nums[cur] > 1:
                right -= 1
                nums[cur], nums[right] = nums[right], nums[cur]
            elif nums[cur] < 1:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            # nums[cur] == 1
            else:
                cur += 1
        return nums

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    answer =[0,0,1,1,2,2]
    sol = Solution()
    result = sol.sortColors(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [0,0,1,1,2,2]
    result: [0,0,1,1,2,2]
    비교: True
    """