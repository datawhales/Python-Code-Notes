""" Nodes, Linked Lists, Stack 구현.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

class myList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head == None:
            return "[]"
        s = "[" + str(self.head)
        t = self.head.next
        while t != None:
            s += ", " + str(t)
            t = t.next
        return s + "]"

    def insert(self, x):
        """ 리스트의 가장 앞에 새로운 노드를 추가하는 메소드.
        """
        new = Node(x)
        new.next = self.head
        if self.head != None:
            self.head.prev = new
        self.head = new
        
    def search(self, d):
        """ data d를 가지는 노드가 있는지 확인하는 메소드.
            Linear search algorithm 이용.
        """
        t = self.head
        while t != None and t.data != d:
            t = t.next
        if t != None:
            return True
        return False
    
    def delete(self, x):
        """ data x를 가지는 첫 번째 노드를 삭제하는 메소드.
        """
        t = self.head
        while t != None and t.data != x:
            t = t.next
        if t != None:
            if t.prev != None:
                t.prev.next = t.next
            else:
                t.next.prev = None
                self.head = t.next
            if t.next != None:
                t.next.prev = t.prev
            else:
                t.prev.next = None
                self.tail = t.prev

class Stack:
    def __init__(self):
        self.sentinel = Node(0)
        self.size = 0
    
    def push(self, x):
        self.size += 1
        new = Node(x)
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