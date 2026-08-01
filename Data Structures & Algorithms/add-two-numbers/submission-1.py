# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=""
        str2=""
        while l1!=None or l2!=None:
            if l1!=None:
                str1=str1+str(l1.val)
                l1=l1.next
            if l2!=None:
                str2=str2+str(l2.val)
                l2=l2.next
        str1=str1[::-1]
        str2=str2[::-1]
        sums=str(int(str1)+int(str2))
        sums=sums[::-1]
        new=ListNode()
        dums=new
        for i in range(len(sums)):
            dums.val=int(sums[i])
            if i==len(sums)-1:
                dums.next=None
                break
            dums.next=ListNode()
            dums=dums.next
        return new
        
