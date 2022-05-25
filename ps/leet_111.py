""" Leetcode.
    111. Minimum Depth of Binary Tree
    Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
    
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        return min(left, right) + 1

    def minDepth_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                tree = queue.popleft()

                if not tree.left and not tree.right:
                    return depth
                if tree.left:
                    queue.append(tree.left)
                if tree.right:
                    queue.append(tree.right)
        return 0

if __name__ == "__main__":
    s = "226"
    answer = 3
    sol = Solution()
    result = sol.numDecodings(s)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """