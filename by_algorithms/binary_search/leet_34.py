""" Leetcode. Binary Search.
    34. Find First and Last Position of Element in Sorted Array
    Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        else:
            first = left
            while left < len(nums) and nums[left] == target:
                left += 1
            return [first, left-1]
        
if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    answer = [3, 4]

    sol = Solution()
    result = sol.searchRange(nums, target)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [3, 4]
    result: [3, 4]
    비교: True
    """