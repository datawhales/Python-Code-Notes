""" Leetcode.
    240. Search a 2D Matrix II
    Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
        
        return False

if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    answer = True
    sol = Solution()
    result = sol.searchMatrix(matrix, target)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """