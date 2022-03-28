""" Leetcode. Backtracking.
    46. Permutations
    Link: https://leetcode.com/problems/permutations/
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        def dfs(nums, path):
            # 종료 조건
            if len(path) == n:
                ret.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        return ret

if __name__ == "__main__":
    nums = [1, 2, 3]
    answer = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    sol = Solution()
    result = sol.permute(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    비교: True
    """