""" Leetcode.
    713. Subarray Product Less Than K
    Link: https://leetcode.com/problems/subarray-product-less-than-k/
"""
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt, product = 0, 1
        start = 0
        for end in range(len(nums)):
            # window의 오른쪽 추가
            product *= nums[end]
            while start <= end and product >= k:
                # window의 왼쪽 제거
                product //= nums[start]
                start += 1
            cnt += end - start + 1
        return cnt

if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    answer = 8
    sol = Solution()
    result = sol.numSubarrayProductLessThanK(nums, k)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 8
    result: 8
    비교: True
    """