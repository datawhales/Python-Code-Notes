""" Leetcode.
    6. Zigzag Conversion
    Link: https://leetcode.com/problems/zigzag-conversion/
"""
from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret = [''] * numRows
        direction = 1
        pointer = 0
        for i in range(len(s)):
            ret[pointer] += s[i]
            pointer += direction
            if pointer < 0 or pointer >= numRows:
                direction *= -1
                pointer += 2 * direction
        return ''.join(ret)

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    answer = "PAHNAPLSIIGYIR"
    sol = Solution()
    result = sol.convert(s, numRows)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: PAHNAPLSIIGYIR
    result: PAHNAPLSIIGYIR
    비교: True
    """