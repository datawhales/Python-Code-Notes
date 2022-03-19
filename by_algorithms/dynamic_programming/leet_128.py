""" Leetcode. DP.
    128. Longest Consecutive Sequence
    Link: https://leetcode.com/problems/longest-consecutive-sequence/
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s, ret = set(nums), 1
        for num in s:
            # 가장 작은 원소에 대해 체크하기 위해
            # 해당 원소보다 1 작은 원소가 존재하는 경우
            # 그 원소에서 체크하면 되므로 패스
            if num - 1 in s:
                continue
            # 그 원소부터 시작하는 경로의 길이 체크
            cnt = 1
            while num + cnt in s:
                cnt += 1
            ret = max(ret, cnt)
        return ret

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    answer = 4
    sol = Solution()
    result = sol.longestConsecutive(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 4
    result: 4
    비교: True
    """