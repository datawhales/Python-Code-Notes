""" Leetcode.
    1091. Shortest Path in Binary Matrix
    Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 처음과 끝이 막혀 있으면 경로 불가능
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        grid[0][0] = 1
        queue = deque([(0, 0)])
        # 방문 처리
        while queue:
            x, y = queue.popleft()
            # 8가지 방향 정의
            dx = [-1, -1, 0, 1, 1, 1, 0, -1]
            dy = [0, 1, 1, 1, 0, -1, -1, -1]
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                    if grid[nx][ny] == 0:
                        # 큐에 삽입 후 방문 처리
                        queue.append((nx, ny))
                        grid[nx][ny] = grid[x][y] + 1
        return grid[-1][-1] if grid[-1][-1] != 0 else -1
        
if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    answer = 4
    sol = Solution()
    result = sol.shortestPathBinaryMatrix(grid)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 4
    result: 4
    비교: True
    """