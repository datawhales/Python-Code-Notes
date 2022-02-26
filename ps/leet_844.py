""" Leetcode. Two Pointers.
    844. Backspace String Compare
    Link: https://leetcode.com/problems/backspace-string-compare/
"""
from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert_string(s):
            ret = []
            for char in s:
                if char == '#':
                    if not ret:
                        continue
                    ret.pop()
                else:
                    ret.append(char)
            return ''.join(ret)
        return convert_string(s) == convert_string(t)
        
if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    answer = True
    sol = Solution()
    result = sol.backspaceCompare(s, t)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: True
    result: True
    비교: True
    """