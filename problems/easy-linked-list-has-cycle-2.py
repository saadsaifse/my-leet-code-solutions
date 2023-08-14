# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if id(head) not in seen:
                seen.add(id(head))
            else:
                if head.next:
                    return head
                return
            head = head.next
            
        return