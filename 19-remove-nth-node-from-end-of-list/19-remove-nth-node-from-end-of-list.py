# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        
        while n > 0:
            right = right.next #this will put the right pointer n-1 positions in front of left pointer
            n -= 1
        
        while right: #once right is null we know left is the n-2 node from the end of the list because left was already 1 behind right and 
            #right is now in the n-1 position so left is n-2
            right = right.next
            left = left.next
        
        left.next = left.next.next #cut out left.next which is the n-1th node from the end of the list, this is because n is 1-indexed by the list is 0-indexed
        return dummy.next #dummy isnt a node from the original list, dummy.next is the head node