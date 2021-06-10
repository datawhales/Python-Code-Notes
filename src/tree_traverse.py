""" Tree 구조 순회하는 메소드 구현.
"""
class TreeNode:
    def __init__(self, x, k):
        self.data = x
        self.arity = k
        self.child = [None] * k

class Tree:
    def __init__(self):
        self.root = None
    
    def visit(self, node: TreeNode):
        print(node.data)

    def BFT(self):
        if self.root == None:
            return
        from collections import deque
        queue = deque([self.root])
        while queue:
            curNode = queue.popleft()
            self.visit(curNode)
            for childNode in curNode.child:
                if childNode:
                    queue.append(childNode)

    def __DFT_preorderHelp(self, curNode: TreeNode):
        if curNode == None:
            return
        self.visit(curNode)
        for childNode in curNode.child:
            self.__DFT_preorderHelp(childNode)

    def DFT_preorder(self):
        self.__DFT_preorderHelp(self.root)

    def __DFT_inorderHelp(self, curNode: TreeNode):
        if curNode == None:
            return
        for i in range(len(curNode.child)):
            if i == 1:
                self.visit(curNode)
            self.__DFT_inorderHelp(curNode.child[i])
    
    def DFT_inorder(self):
        self.__DFT_inorderHelp(self.root)

    def __DFT_postorderHelp(self, curNode: TreeNode):
        if curNode == None:
            return
        for childNode in curNode.child:
            self.__DFT_postorderHelp(childNode)
        self.visit(curNode)