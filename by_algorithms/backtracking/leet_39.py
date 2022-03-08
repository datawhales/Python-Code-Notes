""" Leetcode. Backtracking.
    39. Combination Sum
    Link: https://leetcode.com/problems/combination-sum/
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def dfs(trg, path):
            # 종료 조건
            if trg < 0:
                return
            # 경로 추가 조건
            if trg == 0:
                ret.append(path)
                return
            for n in candidates:
                # 최근에 추가된 수보다 크거나 같은 수만 추가 - 중복 제거하기 위함
                if not path or n >= path[-1]:
                    dfs(trg - n, path + [n])
        dfs(target, [])
        return ret

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    answer = [[2, 2, 3], [7]]
    sol = Solution()
    result = sol.combinationSum(candidates, target)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[2, 2, 3], [7]]
    result: [[2, 2, 3], [7]]
    비교: True
    """