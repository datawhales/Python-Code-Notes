""" Leetcode.
    59. Spiral Matrix II
    Link: https://leetcode.com/problems/spiral-matrix-ii/
"""
from typing import List

class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        x, y = 0, 0
        # 진행하는 방향 설정
        dx, dy = 0, 1
        for i in range(n * n):
            matrix[x][y] = i + 1
            # 진행 방향 변화
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n or matrix[x + dx][y + dy] != 0:
                dx, dy = dy, -dx
            x, y = x + dx, y + dy
        return matrix

if __name__ == "__main__":
    n = 3
    answer = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    sol = Solution()
    result = sol.generateMatrix(n)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    result: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    비교: True
    """