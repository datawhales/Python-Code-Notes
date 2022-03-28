""" Leetcode. Hash Table.
    229. Majority Element II
    Link: https://leetcode.com/problems/majority-element-ii/
"""
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = []
        num_map = defaultdict(int)
        for i in range(n):
            num_map[nums[i]] += 1
        for num in num_map:
            if num_map[num] > n // 3:
                ret.append(num)
        return ret

if __name__ == "__main__":
    nums = [3, 2, 3]
    answer = [3]
    sol = Solution()
    result = sol.majorityElement(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [3]
    result: [3]
    비교: True
    """