""" Leetcode. DP.
    377. Combination Sum IV
    Link: https://leetcode.com/problems/combination-sum-iv/
"""
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        # target보다 작은 n에 대해서만 1 저장
        for n in nums:
            if n <= target:
                dp[n] = 1
        # dynamic programming
        for i in range(1, target+1):
            for n in nums:
                if i-n > 0:
                    dp[i] += dp[i-n]
        return dp[target]

if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    answer = 7
    sol = Solution()
    result = sol.combinationSum4(nums, target)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 7
    result: 7
    비교: True
    """