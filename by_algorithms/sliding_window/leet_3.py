""" Leetcode.
    3. Longest Substring Without Repeating Characters
    Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        # sliding window
        max_len = 0
        left, right = 0, 0
        window = ''
        for i in range(len(s)):
            if s[i] in window:
                left += window.index(s[i]) + 1
                right = i
            else:
                right = i
            window = s[left:right+1]
            if right - left + 1 > max_len:
                max_len = right - left + 1
        return max_len

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        if not s:
            return 0
        start, max_len = 0, 0
        used = {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            used[s[i]] = i
        return max_len

if __name__ == "__main__":
    s = 'pwwkew'
    answer = 3
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """