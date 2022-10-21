# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head
        
        len_of_list = 1
        cur = head
        while cur.next != None:
            cur = cur.next
            len_of_list += 1
        
        # cur now equals last LL item
        cur.next = head # LL is circular
        
        k = len_of_list - (k % len_of_list)
        
        for i in range(0, k):
            cur = cur.next
        
        new_head = cur.next
        cur.next = None
        return new_head