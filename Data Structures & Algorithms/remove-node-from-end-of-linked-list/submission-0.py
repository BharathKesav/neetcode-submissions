# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        j=dummy
        itere=dummy
        for i in range(n):
            j=j.next
        while j.next!=None:
            itere=itere.next
            j=j.next
        itere.next=itere.next.next  
        return dummy.next

        

