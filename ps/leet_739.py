""" Leetcode. Stack.
    739. Daily Temperatures
    Link: https://leetcode.com/problems/daily-temperatures/
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        # 1. 하나씩 스택 안에 넣기 전에 스택의 가장 위쪽에 있는 원소와 비교
        # 2. 비교해서 들어오려고 하는 원소보다 작은 스택 안의 원소들을 모두 꺼낸다 - while
        # 3. 새로운 원소를 넣는다.
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                item = stack.pop()
                ret[item[1]] = i - item[1]
            stack.append((t, i))
        return ret

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    answer = [1,1,4,2,1,1,0,0]
    sol = Solution()
    result = sol.dailyTemperatures(temperatures)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [1,1,4,2,1,1,0,0]
    result: [1,1,4,2,1,1,0,0]
    비교: True
    """
