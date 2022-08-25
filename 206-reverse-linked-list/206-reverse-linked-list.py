# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursive(head, None)
        #return self.iterative(head)
    
    def iterative(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        
        return curr
    def recursive(self, head, prev) -> Optional[ListNode]:
        if not head:
            return prev
        _next = head.next
        head.next = prev
        return self.recursive(_next, head)