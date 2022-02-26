""" Leetcode. Two Pointers.
    986. Interval List Intersections
    Link: https://leetcode.com/problems/interval-list-intersections/
"""
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = []
        first, second = 0, 0
        while first < len(firstList) and second < len(secondList):
            tmp_first, tmp_second = firstList[first], secondList[second]
            if (tmp_first[0] < tmp_second[0] and tmp_first[1] < tmp_second[0]):
                first += 1
                continue
            elif (tmp_second[0] < tmp_first[0] and tmp_second[1] < tmp_first[0]):
                second += 1
                continue
            else:
                ret.append([max(tmp_first[0], tmp_second[0]), min(tmp_first[1], tmp_second[1])])
                if tmp_first[1] < tmp_second[1]:
                    first += 1
                elif tmp_second[1] < tmp_first[1]:
                    second += 1
                else:
                    first += 1
                    second += 1
        return ret
        
if __name__ == "__main__":
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    answer = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    sol = Solution()
    result = sol.intervalIntersection(firstList, secondList)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    result: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    비교: True
    """