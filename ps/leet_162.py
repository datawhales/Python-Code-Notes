""" Leetcode. Binary Search.
    162. Find Peak Element
    Link: https://leetcode.com/problems/find-peak-element/
"""
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid] > nums[mid-1]) \
            and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid] < nums[mid-1]:
                right = mid - 1
        
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    answer = 2

    sol = Solution()
    result = sol.findPeakElement(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """