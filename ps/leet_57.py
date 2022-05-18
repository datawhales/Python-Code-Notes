""" Leetcode.
    57. Insert Interval
    Link: https://leetcode.com/problems/insert-interval/
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ret = []
        i = -1
        
        for i, (x, y) in enumerate(intervals):
            if y < newInterval[0]:
                ret.append([x, y])
            
            elif x > newInterval[1]:
                i -= 1
                break
            
            else:
                newInterval[0] = min(x, newInterval[0])
                newInterval[1] = max(y, newInterval[1])
                
        return ret + [newInterval] + intervals[i+1:]

if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    answer = [[1,2],[3,10],[12,16]]
    sol = Solution()
    result = sol.insert(intervals, newInterval)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[1, 2], [3, 10], [12, 16]]
    result: [[1, 2], [3, 10], [12, 16]]
    비교: True
    """