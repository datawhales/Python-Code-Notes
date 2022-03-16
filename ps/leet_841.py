""" Leetcode. DFS.
    841. Keys and Rooms
    Link: https://leetcode.com/problems/keys-and-rooms/
"""
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        def dfs(x, visited):
            if not visited[x]:
                visited[x] = True
                for i in rooms[x]:
                    dfs(i, visited)
        dfs(0, visited)
        return all(visited)

if __name__ == "__main__":
    rooms = [[1],[2],[3],[]]
    answer = True
    sol = Solution()
    result = sol.canVisitAllRooms(rooms)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """