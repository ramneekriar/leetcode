from typing import Optional

from networkx import second_order_centrality

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # ex: 1 -> 2 -> 3 -> 4 -> 5 -> None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is pointing to 3
        # we need to reverse everything from slow.next inclusive

        second = slow.next # second = 4 -> 5 -> None
        slow.next = None # End first half of list to avoid loop, 1 -> 2 -> 3 -> None
        node = None # the reversed list will be built here

        while second:
            temp = second.next # 5 -> None | None
            second.next = node # 4 -> None | 5 -> 4 -> None
            node = second # 4 -> None | 5 -> 4 -> None
            second = temp # 5 -> None | None
        
        first = head # 1 -> 2 -> 3 -> None
        second = node # 5 -> 4 -> None

        while second:
            temp1 = first.next # 2 -> ... | 3 -> ...
            temp2 = second.next # 4 -> ... | None
            first.next, second.next = second, temp1 # 1 -> 5 -> 2 -> 3 -> None | # 1 -> 5 -> 2 -> 4 -> 3 -> None
            first, second = temp1, temp2 # 2 -> ..., 4 -> None | 3 -> None, None
        


