""" Leetcode.
    48. Rotate Image
    Link: https://leetcode.com/problems/rotate-image/
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        return matrix

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    answer = [[7,4,1],[8,5,2],[9,6,3]]
    sol = Solution()
    result = sol.rotate(matrix)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    result: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    비교: True
    """