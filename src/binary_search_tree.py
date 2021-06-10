class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __searchHelp(self, curNode: TreeNode, x) -> TreeNode:
        if not curNode:
            return None
        if x == curNode.data:
            return curNode
        elif x < curNode.data:
            return self.__searchHelp(curNode.left, x)
        else:
            return self.__searchHelp(curNode.right, x)
    
    def search(self, x):
        return self.__searchHelp(self.root, x)

    def __insertHelp(self, curNode: TreeNode, x) -> TreeNode:
        if not curNode:
            return TreeNode(x)
        if x < curNode.data:
            curNode.left = self.__insertHelp(curNode.left, x)
        else:
            curNode.right = self.__insertHelp(curNode.right, x)

    def insert(self, x):
        self.root = self.__insertHelp(self.root, x)

    # def __traverseHelp(self, curNode):
    #     result = []
    #     if curNode.left:
    #         result.extend(self.__traverseHelp(curNode.left))
    #     if curNode:
    #         result.extend([curNode.data])
    #     if curNode.right:
    #         result.extend(self.__traverseHelp(curNode.right))
    #     return result

    # def traverse(self):
    #     return self.__traverseHelp(self.root)


    # def __deleteHelp(self, curNode: TreeNode, x) -> TreeNode:
    #     if x == curNode.data:
    #         pass

    #     elif x < curNode.data:
    #         if curNode.left.data == x:
    #             if not curNode.left.left and not curNode.left.right:
    #                 curNode.left = None
    #             elif curNode.left.left and not curNode.left.right:
    #                 pass
    #             elif not curNode.left.left and curNode.left.right:
    #                 pass
    #             else:
    #                 pass
    #         elif curNode.left.data < x:
    #             pass
    #         else:
    #             pass
    #     elif x > curNode.data:
    #         if curNode.right.data == x:
    #             if not curNode.right.left and not curNode.right.right:
    #                 curNode.right = None
    #             elif curNode.right.left and not curNode.right.right:
    #                 pass
    #             elif not curNode.right.left and curNode.right.right:
    #                 pass
    #             else:
    #                 pass
    #         elif curNode.right.data < x:
    #             pass
    #         else:
    #             pass

    # def delete(self, x):
    #     return self.__deleteHelp(self.root, x)