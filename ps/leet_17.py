""" Leetcode.
    17. Letter Combinations of a Phone Number
    Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_map = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        ret = []
        n = len(digits)
        def dfs(digits, path):
            # ret에 path 추가 조건
            if len(path) == n:
                ret.append(path)
            for i in range(len(digits)):
                for j in range(len(digits_map[digits[i]])):
                    dfs(digits[i+1:], path + [digits_map[digits[i]][j]])
        dfs(digits, [])
        return [''.join(x) for x in ret]

if __name__ == "__main__":
    digits = "23"
    answer = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    sol = Solution()
    result = sol.letterCombinations(digits)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    비교: True
    """