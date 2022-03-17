""" Leetcode. DP.
    1014. Best Sightseeing Pair
    Link: https://leetcode.com/problems/best-sightseeing-pair/
"""
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # 두 숫자 중 왼쪽 숫자의 인덱스
        left = 0
        dp = [0] * len(values)
        for i in range(1, len(values)):
            # 왼쪽 숫자의 최대값 업데이트
            if values[i-1] + i-1 > values[left] + left:
                left = i-1
            # score 계산하여 더 큰 값을 저장
            if values[left] + left + values[i] - i > dp[i-1]:
                dp[i] = values[left] + left + values[i] - i
            else:
                dp[i] = dp[i-1]
        return dp[-1]

if __name__ == "__main__":
    values = [8,1,5,2,6]
    answer = 11
    sol = Solution()
    result = sol.maxScoreSightseeingPair(values)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 11
    result: 11
    비교: True
    """