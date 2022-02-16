""" Leetcode. DP.
    300. Longest Increasing Subsequence
    Link: https://leetcode.com/problems/longest-increasing-subsequence/
"""
from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_2(self, nums: List[int]) -> int:
        path = []
        for x in nums:
            if len(path) == 0 or path[-1] < x:
                path.append(x)
            else:
                idx = bisect_left(path, x)
                path[idx] = x
        return len(path)

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    answer = 4

    sol = Solution()
    result = sol.lengthOfLIS(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 4
    result: 4
    비교: True
    """