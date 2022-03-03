""" Leetcode.
    47. Permutations II
    Link: https://leetcode.com/problems/permutations-ii/
"""
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(nums, path):
            # 수행 작업
            if not nums:
                ret.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
        # sort 해야 중복 제거 가능
        dfs(sorted(nums), [])
        return ret

if __name__ == "__main__":
    nums = [1, 2, 3]
    answer = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    sol = Solution()
    result = sol.permuteUnique(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    비교: True
    """