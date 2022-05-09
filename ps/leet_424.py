""" Leetcode. Sliding Window.
    424. Longest Repeating Character Replacement
    Link: https://leetcode.com/problems/longest-repeating-character-replacement/
"""
from typing import List
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s를 순회하면서
        # 알파벳 개수를 카운트
        # 투포인터 활용
        # right-left-가장 많은 빈도의 알파벳 개수 <= k일 때 max_len 측정
        
        if len(s) <= k:
            return len(s)
        
        max_len = 0
        left = 0
        freq = defaultdict(int)
        
        for i, char in enumerate(s):
            right = i + 1
            freq[char] += 1

            if right - left - max(freq.values()) <= k:
                max_len = max(max_len, right - left)
            
            else:
                while left < right and right - left - max(freq.values()) > k:
                    freq[s[left]] -= 1
                    left += 1
                    
        return max_len

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    answer = 4
    sol = Solution()
    result = sol.characterReplacement(s, k)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 4
    result: 4
    비교: True
    """