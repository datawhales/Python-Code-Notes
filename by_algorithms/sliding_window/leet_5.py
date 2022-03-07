""" Leetcode. DP.
    5. Longest Palindromic Substring
    Link: https://leetcode.com/problems/longest-palindromic-substring/
"""
from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming
        ret = ''
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            ret = s[i]
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if i + 1 == j or dp[i+1][j-1]:
                        dp[i][j] = True
                        if len(ret) <= len(s[i:j+1]):
                            ret = s[i:j+1]
        return ret
        
    def longestPalindrome_2(self, s: str) -> str:
        ret = s[0]
        for left in range(len(s)):
            right = len(s) - 1
            while left <= right:
                if s[left] != s[right]:
                    right -= 1
                    continue
                if right - left >= len(ret) and s[left:right+1] == s[left:right+1][::-1]:
                    ret = s[left:right+1]
                else:
                    right -= 1
        return ret

    def longestPalindrome_3(self, s: str) -> str:
        # 중앙으로부터 팰린드롬을 유지하면서 확장하는 함수
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        # 문자열의 길이가 1이거나 전체가 팰린드롬인 경우 그대로 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        ret = ''
        for i in range(len(s) - 1):
            # 중앙이 xx 형태인 경우로부터 최대로 확장
            if len(expand(i, i+1)) > len(ret):
                ret = expand(i, i+1)
            # 중앙이 xyx 형태인 경우로부터 최대로 확장
            if len(expand(i, i+2)) > len(ret):
                ret = expand(i, i+2) 
        return ret

if __name__ == "__main__":
    s = "babad"
    answer = "bab"
    sol = Solution()
    result = sol.longestPalindrome(s)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: bab
    result: bab
    비교: True
    """