""" Leetcode.
    54. Spiral Matrix
    Link: https://leetcode.com/problems/rotate-image/
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        dx, dy = 0, 1
        
        # dx, dy = dy, -dx
        
        ret = []
        visited = set()
        x, y = 0, 0
        visited.add((x, y))
        ret.append(matrix[x][y])
        
        for _ in range(m * n - 1):
            # 만약 다음 위치가 visited에 존재하면 방향 전환
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in visited:
                dx, dy = dy, -dx
            
                # 바뀐 방향으로 다시 전진
                x += dx
                y += dy
                
            else:
                x, y = nx, ny
                
            visited.add((x, y))
            ret.append(matrix[x][y])
    
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