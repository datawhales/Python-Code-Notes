""" Leetcode. DP.
    740. Delete and Earn
    Link: https://leetcode.com/problems/delete-and-earn/
"""
from typing import List
from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for n in nums:
            table[n] += 1
        dp = [0] * (max(nums) + 1)
        dp[1] = table[1]
        # i-1을 포함하고 있으면 i는 포함 불가능
        # i-1을 포함하고 있지 않으면 i-2의 값에 더함
        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i-2] + table[i] * i, dp[i-1])
        return dp[-1]

if __name__ == "__main__":
    nums = [2, 2, 3, 3, 3, 4]
    answer = 9
    sol = Solution()
    result = sol.deleteAndEarn(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 9
    result: 9
    비교: True
    """