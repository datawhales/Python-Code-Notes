""" Leetcode.
    54. Spiral Matrix
    Link: https://leetcode.com/problems/rotate-image/
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        
        dx, dy = 0, 1
        x, y = 0, 0
        ret = []
        for _ in range(m*n):
            visited[x][y] = True
            ret.append(matrix[x][y])
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                dx, dy = dy, -dx
            x += dx
            y += dy
        return ret

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    answer = [1,2,3,6,9,8,7,4,5]
    sol = Solution()
    result = sol.spiralOrder(matrix)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    result: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    비교: True
    """