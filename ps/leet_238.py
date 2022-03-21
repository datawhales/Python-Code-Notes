""" Leetcode.
    238. Product of Array Except Self
    Link: https://leetcode.com/problems/product-of-array-except-self/
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        left, right = 1, 1
        # 각 위치의 왼쪽 부분과 오른쪽 부분을 따로 구분하여 곱
        for i in range(len(nums)):
            ret[i] *= left
            ret[-i-1] *= right
            left *= nums[i]
            right *= nums[-i-1]
        return ret

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    answer = [24, 12, 8, 6]
    sol = Solution()
    result = sol.productExceptSelf(nums)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [24, 12, 8, 6]
    result: [24, 12, 8, 6]
    비교: True
    """