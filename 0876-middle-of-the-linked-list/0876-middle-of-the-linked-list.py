from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.next
    
# Time = O(n), Space = O(1)