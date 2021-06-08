""" Nodes, Linked Lists, Stack 구현.
"""
class LinkedNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkedLists:
    def __init__(self):
        self.sentinel = LinkedNode(0)
        self.size = 0

    def addFirst(self, x):
        new = LinkedNode(x)
        new.next = self.sentinel.next.next
        self.sentinel.next = new
        self.size += 1

    def getFirst(self):
        return self.sentinel.next.val

    def getSize(self):
        return self.size

    def append(self, x):
        self.size += 1
        curNode = self.sentinel
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = LinkedNode(x)

class Stack:
    def __init__(self):
        self.sentinel = LinkedNode(0)
        self.size = 0
    
    def push(self, x):
        self.size += 1
        new = LinkedNode(x)
        curNode = self.sentinel
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = new

    def pop(self):
        self.size -= 1
        curNode = self.sentinel
        while curNode.next.next != None:
            curNode = curNode.next
        curNode.next = None

    def top(self):
        curNode = self.sentinel
        while curNode.next != None:
            curNode = curNode.next
        return curNode.val

    def getSize(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False