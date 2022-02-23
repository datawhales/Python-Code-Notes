""" Leetcode. Linked List. Two Pointers.
    82. Remove Duplicates from Sorted List II
    Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_listnode(head: List[int]) -> ListNode:
    for i in range(len(head)):
        if i == 0:
            head_node = ListNode(head[i])
            node = head_node
            continue
        node.next = ListNode(head[i])
        node = node.next
    return head_node

def listnode2list(head: ListNode) -> List[int]:
    ret = []
    node = head
    while node:
        ret.append(node.val)
        node = node.next
    return ret
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ret = []
        node, tmp, cnt = head, head.val, 1
        node = node.next
        while node:
            if node.val != tmp:
                if cnt == 1:
                    ret.append(tmp)
                tmp = node.val
                cnt = 1
            else:
                cnt += 1
            node = node.next
            
        if cnt == 1:
            ret.append(tmp)
        
        if not ret:
            return None
        
        for i in range(len(ret)):
            if i == 0:
                head_node = ListNode(ret[i])
                node = head_node
                continue
            node.next = ListNode(ret[i])
            node = node.next
        return head_node

    def deleteDuplicates_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sent = ListNode(-1)
        sent.next = head
        prev, curr = sent, head
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                tmp_value = curr.val
                while curr and curr.val == tmp_value:
                    curr = curr.next
                prev.next = curr
            else:
                prev, curr = curr, curr.next
        return sent.next

if __name__ == "__main__":
    head = [1, 2, 3, 3, 4, 4, 5]
    answer = [1, 2, 5]

    sol = Solution()
    result = listnode2list(sol.deleteDuplicates(get_listnode(head)))

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [1, 2, 5]
    result: [1, 2, 5]
    비교: True
    """