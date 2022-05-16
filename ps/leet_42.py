""" Leetcode.
   42. Trapping Rain Water
    Link: https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_h = max(height)
        
        ret = 0
        # 0 - left_max
        cur = 0
        tmp_max = 0
        while cur < len(height):
            if height[cur] == max_h:
                left_max = cur
                break
            if height[cur] > tmp_max:
                tmp_max = height[cur]
            else:
                ret += tmp_max - height[cur]
            cur += 1    
        # len(height)-1 - right_max
        cur = len(height) - 1
        tmp_max = 0
        while cur >= 0:
            if height[cur] == max_h:
                right_max = cur
                break
            if height[cur] > tmp_max:
                tmp_max = height[cur]
            else:
                ret += tmp_max - height[cur]
            cur -= 1  
        # left_max - right_max
        for i in range(left_max, right_max+1):
            ret += max_h - height[i]
        
        return ret

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    answer = 6
    sol = Solution()
    result = sol.trap(height)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 6
    result: 6
    비교: True
    """