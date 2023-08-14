# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# using two pointer technique. Reference: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1211/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slowNode, fastNode = head, head.next
        while slowNode and fastNode and slowNode.next and fastNode.next:
            if slowNode == fastNode:
                return True

            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return False