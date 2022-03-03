""" Leetcode.
    90. Subsets II
    Link: https://leetcode.com/problems/subsets-ii/
"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(nums, path):
            ret.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], path + [nums[i]])
        dfs(sorted(nums), [])
        return ret

if __name__ == "__main__":
    nums = [1, 2, 2]
    answer = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    sol = Solution()
    result = sol.subsetsWithDup(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    result: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    비교: True
    """