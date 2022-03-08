""" Leetcode. DFS.
    733. Flood Fill
    Link: https://leetcode.com/problems/flood-fill/
"""
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # first color check
        color = image[sr][sc]
        visited = [[False] * len(image[0]) for _ in range(len(image))]
        def dfs(x, y):
            # 종료 조건
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return
            if visited[x][y] or image[x][y] != color:
                return
            # visit
            visited[x][y] = True
            image[x][y] = newColor
            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                dfs(nx, ny)
        dfs(sr, sc)
        return image

if __name__ == "__main__":
    image = [[1, 1, 1],[1, 1, 0],[1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    answer = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    sol = Solution()
    result = sol.floodFill(image, sr, sc, newColor)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    result: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    비교: True
    """