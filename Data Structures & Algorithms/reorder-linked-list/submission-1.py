class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        while second != None:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        first,last=head,prev
        while last!=None:
            temp1,temp2=first.next,last.next
            first.next=last
            last.next=temp1
            first,last=temp1,temp2
           