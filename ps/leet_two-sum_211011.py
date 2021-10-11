""" Leetcode.
    1. Two Sum.
    Link: https://leetcode.com/problems/two-sum/
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 가장 생각하기 쉬운 간단한 풀이.
            Brute Force를 이용.
            nums를 한 번 지나가면서 각 element에 대해 target - element 값이 존재하는지 찾는다.
            Time Complexity: O(n^2)
            Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """ Array의 값과 인덱스를 함께 저장하기에 좋은 방법 => hash table 이용.
            첫 번째 iteration loop을 통해 hash table에 target - nums[i] 값을 인덱스와 함께 저장.
            두 번째 iteration loop을 돌면서 hash table에 원하는 값이 있는지 확인.
            Time Complexity: O(2n) -> O(n)
            Space Complexity: O(n)
        """
        nums_pair = {}
        for i in range(len(nums)):
            nums_pair[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in nums_pair and nums_pair[nums[i]] != i:
                return [i, nums_pair[nums[i]]]

    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        """ Hash table을 이용하면서 iteration loop을 한 번만 돈다.
            Iteration loop을 돌면서 hash table에 값을 저장하는 동시에,
            기존에 찾는 값이 현재까지의 hash table에 저장되어 있는지 확인.
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        nums_pair = {}
        for i, n in enumerate(nums):
            if n in nums_pair:
                return [nums_pair[n], i]
            nums_pair[target - n] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    answer = [0, 1]

    sol = Solution()
    result = sol.twoSum_3(nums, target)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [0, 1]
    result: [0, 1]
    비교: True
    """