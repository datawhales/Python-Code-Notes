""" Leetcode.
    78. Subsets
    Link: https://leetcode.com/problems/subsets/
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [i + [num] for i in res]
        return res

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        pre = self.subsets(nums[:-1])
        return pre + [p + [nums[-1]] for p in pre]

    def subsets_3(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(nums, path):
            ret.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        return ret

if __name__ == "__main__":
    nums = [1, 2, 3]
    answer = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    sol = Solution()
    result = sol.subsets(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    result: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    비교: True
    """