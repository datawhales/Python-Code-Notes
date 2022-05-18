""" Leetcode.
    60. Permutation Sequence
    Link: https://leetcode.com/problems/permutation-sequence/
"""
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ret = ''
        # n!을 계산하여 fac에 저장
        fac = 1
        for i in range(1, n+1):
            fac *= i
        
        # n! -> (n-1)! -> .. 순서대로 계산하기 위해 t에 n 저장
        t = n
        while fac > 1:
            fac //= t
            for i in range(1, n+1):
                if str(i) in ret:
                    continue
                if k - fac > 0:
                    k -= fac
                    continue
                else:
                    ret += str(i)
                    break
            t -= 1
        
        for i in range(1, n+1):
            if str(i) in ret:
                continue
            else:
                ret += str(i)
        return ret

if __name__ == "__main__":
    n = 4
    k = 9
    answer = "2314"
    sol = Solution()
    result = sol.getPermutation(n, k)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2314
    result: 2314
    비교: True
    """