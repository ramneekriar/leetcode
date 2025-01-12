class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n steps ahead, so that when it reaches the end, 
        # slow will point to the node just before nth node
        k = 0
        while k < n:
            fast = fast.next
            k += 1
        
        # Move both slow and fast pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next

# Time = O(n), Space = O(1)