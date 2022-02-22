""" Leetcode. Binary Search.
    33. Search in Rotated Sorted Array
    Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    answer = 4

    sol = Solution()
    result = sol.search(nums, target)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 4
    result: 4
    비교: True
    """