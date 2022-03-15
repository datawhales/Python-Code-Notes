""" Leetcode. DFS.
    934. Shortest Bridge
    Link: https://leetcode.com/problems/shortest-bridge/
"""
from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(x, y, grid):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return False
            if grid[x][y] == 1:
                grid[x][y] = 2
                dx = [0, 1, 0, -1]
                dy = [1, 0, -1, 0]
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    dfs(nx, ny, grid)
                return True
            return False

        # island 중 하나를 2로 페인팅 -> island는 각각 1과 2로 표현됨
        painted = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    painted = dfs(i, j, grid)
                    break
            if painted:
                break
        
        color = 2
        while True:
            for x in range(n):
                for y in range(n):
                    # 3부터 순차적으로 색칠
                    if grid[x][y] == color:
                        dx = [0, 1, 0, -1]
                        dy = [1, 0, -1, 0]
                        for i in range(4):
                            nx, ny = x + dx[i], y + dy[i]
                            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                continue
                            if grid[nx][ny] == 0:
                                grid[nx][ny] = color + 1
                            # 두 번째 island를 의미하는 1을 만난 경우 종료
                            if grid[nx][ny] == 1:
                                return color - 2
            color += 1

if __name__ == "__main__":
    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    answer = 1
    sol = Solution()
    result = sol.shortestBridge(grid)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 1
    result: 1
    비교: True
    """