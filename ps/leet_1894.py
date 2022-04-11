""" Leetcode. Binary Search.
    1894. Find the Student that Will Replace the Chalk
    Link: https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
"""
from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # 누적 합 계산
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i-1]
        n, chalk_sum = len(chalk), chalk[-1]
        target = k % chalk_sum
        target = chalk_sum if target == 0 else target
        # binary search
        start, end = 0, n-1
        while start <= end:
            mid = (start + end) // 2
            if chalk[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if start < n and chalk[start] == target:
            return (start + 1) % n
        else:
            return start

if __name__ == "__main__":
    chalk = [5,1,5]
    k = 22
    answer = 0
    sol = Solution()
    result = sol.chalkReplacer(chalk, k)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 0
    result: 0
    비교: True
    """