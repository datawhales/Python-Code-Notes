""" Leetcode. Binary Search.
    74. Search a 2D Matrix
    Link: https://leetcode.com/problems/search-a-2d-matrix/
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid // n][mid % n] < target:
                left = mid + 1
            else:
                right = mid
        if left < m * n and matrix[left // n][left % n] == target:
            return True
        else:
            return False
        
    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:   
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while up <= down:
            mid_ud = (up + down) // 2
            if matrix[mid_ud][0] < target:
                up = mid_ud + 1
            else:
                down = mid_ud - 1
        if up < len(matrix) and matrix[up][0] == target:
            return True
        else:
            while left <= right:
                mid_lr = (left + right) // 2
                if matrix[down][mid_lr] < target:
                    left = mid_lr + 1
                else:
                    right = mid_lr - 1
            if left < len(matrix[0]) and matrix[down][left] == target:
                return True
            else:
                return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    answer = True

    sol = Solution()
    result = sol.searchMatrix(matrix, target)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """