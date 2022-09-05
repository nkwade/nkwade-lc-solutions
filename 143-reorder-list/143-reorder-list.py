# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:    
        slow, fast = head, head.next    
        while fast and fast.next: #this loop gets slow in the middle of the list because fast moves twice as fast as slow
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next#start of the second half of the list
        prev = slow.next = None#splits the list in half by nulling the next node
        
        while second:#while the second half of the list is not null
            #this loop reverses the second half of the list: n, n-1, n-2 etc
            tmp = second.next #second.next will be modified so we store the value
            second.next = prev #this sets the next to the previous essentially swapping the two nodes, reversing the list
            prev = second #now the previous node is the current node setting up another swap
            second = tmp #shifts the node to be swapped to the right
        
        first, second = head, prev #take the heads of the two lists
        while second:#the second half is going to be equal length or one node longer so second will run out first
            tmp1, tmp2 = first.next, second.next #store the two next nodes for the lists
            first.next = second#merge the second half into the first
            second.next = tmp1 #now that the second node is in the first half, make its next value the first nodes original next value
            first, second = tmp1, tmp2#update the two heads