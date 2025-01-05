# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        return newHead

# Time = O(n), Space = O(1)