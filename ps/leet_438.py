""" Leetcode.
    438. Find All Anagrams in a String
    Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        count_dict = defaultdict(int)
        for char in p:
            count_dict[char] += 1
        for i in range(len(s) - len(p) + 1):
            if i == 0:
                tmp_count = defaultdict(int)
                window = s[i:i+len(p)]
                for char in window:
                    tmp_count[char] += 1
                if count_dict == tmp_count:
                    ret.append(i)
            else:
                tmp_count[s[i+len(p)-1]] += 1
                tmp_count[s[i-1]] -= 1
                if tmp_count[s[i-1]] == 0:
                    tmp_count.pop(s[i-1])
                if count_dict == tmp_count:
                    ret.append(i)
        return ret

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    answer = [0, 6]
    sol = Solution()
    result = sol.findAnagrams(s, p)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [0, 6]
    result: [0, 6]
    비교: True
    """