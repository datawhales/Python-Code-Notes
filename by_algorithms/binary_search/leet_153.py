""" Leetcode. Binary Search.
    153. Find Minimum in Rotated Sorted Array
    Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        
        return nums[start]
        
if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    answer = 1

    sol = Solution()
    result = sol.findMin(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 1
    result: 1
    비교: True
    """