""" Leetcode. Sliding Window.
    424. Longest Repeating Character Replacement
    Link: https://leetcode.com/problems/longest-repeating-character-replacement/
"""
from typing import List
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s의 각 원소를 순회하면서 카운터에 개수를 추가
        # right - left - 카운터에서 가장 빈도 수가 높은 원소의 개수 <= k 이면 right += 1
        # 다시 k가 될 때까지 left += 1, 카운터에서 s[left] 값의 빈도 수도 -= 1
        
        left = 0
        max_num = 0
        freq = Counter()
        
        for right, char in enumerate(s, 1):
            freq[char] += 1
            
            if right - left - max(freq.values()) <= k:
                max_num = max(max_num, right - left)
            
            else:        
                while left <= right and right - left - max(freq.values()) > k:
                    freq[s[left]] -= 1
                    left += 1
            
        return len(s) if max_num == 0 else max_num

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