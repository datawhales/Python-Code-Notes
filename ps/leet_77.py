""" Leetcode. Backtracking.
    77. Combinations
    Link: https://leetcode.com/problems/combinations/
"""
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        
        def dfs(nums, k, path):
            if k == 0:
                ret.append(path)
                return
            
            for i in range(len(nums)):
                dfs(nums[i+1:], k-1, path + [nums[i]])
    
        dfs([i for i in range(1, n+1)], k, [])
        
        return ret

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        def dfs(n, k):
            if k == 1:
                return [[i] for i in range(1, n+1)]
            if n == k:
                return [[i for i in range(1,k+1)]]
            
            ret = []
            ret += dfs(n-1, k)
            rest = dfs(n-1, k-1)
            for pair in rest:
                pair.append(n)
            ret += rest
            
            return ret
        
        return dfs(n, k)

if __name__ == "__main__":
    n = 4
    k = 2
    answer = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    sol = Solution()
    result = sol.combine(n, k)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    result: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    비교: True
    """