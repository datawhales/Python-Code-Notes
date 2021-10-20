""" Leetcode.
    217. Contains Duplicate
    Link: https://leetcode.com/problems/contains-duplicate/
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_table = {}
        for i, n in enumerate(nums):
            if n in check_table:
                return True
            else:
                check_table[n] = 1
        return False
        
    def containsDuplicate_2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    answer = True

    sol = Solution()
    result = sol.containsDuplicate(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """