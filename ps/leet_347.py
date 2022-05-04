""" Leetcode.
    347. Top K Frequent Elements
    Link: https://leetcode.com/problems/top-k-frequent-elements/
"""
from typing import List
from collections import defaultdict
import heapq
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        
        for i in range(len(nums)):
            freq[nums[i]] += 1
    
        heap = []
        for x in freq:
            heapq.heappush(heap, (-freq[x], x))
        
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        
        return ret

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    answer = [1, 2]
    sol = Solution()
    result = sol.topKFrequent(nums, k)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [1, 2]
    result: [1, 2]
    비교: True
    """