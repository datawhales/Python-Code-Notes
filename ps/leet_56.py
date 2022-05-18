""" Leetcode.
    56. Merge Intervals
    Link: https://leetcode.com/problems/merge-intervals/
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ret = []
        i = 1
        tmp = intervals[0]
        while i < len(intervals):
            if tmp[1] < intervals[i][0]:
                ret.append(tmp)
                tmp = intervals[i]
                i += 1
            else:
                tmp = [tmp[0], max(tmp[1], intervals[i][1])]
                i += 1
        ret.append(tmp)
        return ret

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    answer = [[1, 6], [8, 10], [15, 18]]
    sol = Solution()
    result = sol.merge(intervals)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[1, 6], [8, 10], [15, 18]]
    result: [[1, 6], [8, 10], [15, 18]]
    비교: True
    """