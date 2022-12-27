""" Leetcode. Linked List.
    19. Remove Nth Node From End of List
    Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        slow, fast = dummy, dummy
        
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return None
        while fast.next:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    n = 2
    answer = [1, 2, 3, 5]

    sol = Solution()
    result = listnode2list(sol.removeNthFromEnd(get_listnode(head), n))

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [1, 2, 3, 5]
    result: [1, 2, 3, 5]
    비교: True
    """
