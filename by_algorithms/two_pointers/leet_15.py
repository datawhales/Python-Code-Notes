""" Leetcode. Two Pointers.
    15. 3Sum
    Link: https://leetcode.com/problems/3sum/
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ret
        
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    answer = [[-1, -1, 2], [-1, 0, 1]]
    sol = Solution()
    result = sol.threeSum(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[-1, -1, 2], [-1, 0, 1]]
    result: [[-1, -1, 2], [-1, 0, 1]]
    비교: True
    """
