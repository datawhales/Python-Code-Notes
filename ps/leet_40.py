""" Leetcode. Backtracking.
    40. Combination Sum II
    Link: https://leetcode.com/problems/combination-sum-ii/
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        ret = []
        def dfs(nums, trg, path):
            if trg == 0:
                ret.append(path)
                return
        
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if nums[i] <= trg:
                    dfs(nums[i+1:], trg - nums[i], path + [nums[i]])
            
        dfs(candidates, target, [])
    
        return ret

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    answer = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    sol = Solution()
    result = sol.combinationSum2(candidates, target)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    result: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    비교: True
    """