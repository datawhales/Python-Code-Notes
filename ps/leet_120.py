""" Leetcode. DP.
    120. Triangle
    Link: https://leetcode.com/problems/triangle/
"""
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * i for i in range(1, len(triangle)+1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i+1):
                # 양 끝에 위치한 경우 그대로 더함
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                # 양 끝이 아닌 경우 그 위치에 도달할 수 있는 위치 중 최솟값에 더함
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])

if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    answer = 11
    sol = Solution()
    result = sol.minimumTotal(triangle)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 11
    result: 11
    비교: True
    """