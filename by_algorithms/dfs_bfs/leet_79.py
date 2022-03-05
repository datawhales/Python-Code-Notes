""" Leetcode.
    79. Word Search
    Link: https://leetcode.com/problems/word-search/
"""
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        ret = ''
        def dfs(x, y, path):
            nonlocal ret
            print(f'dfs {x}, {y}, {path}, {ret}')
            print(visited)
            # 경로가 알맞게 가고 있지 않거나 이미 단어가 발견되었다면 바로 종료
            if ret == word or path != word[:len(path)]:
                return
            # 경로가 타겟 단어와 같다면 ret에 단어 추가하고 종료
            if path == word:
                ret += path
                return
            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                    continue
                # 다음 step의 dfs 진행 시에는 지난 위치 체크
                visited[x][y] = True
                if not visited[nx][ny]:
                    dfs(nx, ny, path + board[nx][ny])
                # 다음 step의 dfs 종료 후에는 다시 지나지 않은 것으로 변경하여 백트래킹할 수 있도록 함
                visited[x][y] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, board[i][j])
        return ret == word
                
if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    answer = True
    sol = Solution()
    result = sol.exist(board, word)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """