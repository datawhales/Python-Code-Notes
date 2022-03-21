""" Leetcode. Greedy.
    334. Increasing Triplet Subsequence
    Link: https://leetcode.com/problems/increasing-triplet-subsequence/
"""
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            # elif num <= second:
            elif num > first and num <= second:
                second = num
            # else:
            elif num > second:
                return True

if __name__ == "__main__":
    nums = [2, 1, 5, 0, 4, 6]
    answer = True
    sol = Solution()
    result = sol.increasingTriplet(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """