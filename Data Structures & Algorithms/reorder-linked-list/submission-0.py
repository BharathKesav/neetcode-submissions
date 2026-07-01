class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Store values
        lis = []
        temp = head
        while temp:
            lis.append(temp.val)
            temp = temp.next

        # Create reordered values
        lis2 = []
        i = 0
        j = len(lis) - 1

        while i < j:
            lis2.append(lis[i])
            lis2.append(lis[j])
            i += 1
            j -= 1

        if i == j:
            lis2.append(lis[i])

        # Rewrite existing list
        temp = head
        k = 0
        while temp:
            temp.val = lis2[k]
            temp = temp.next
            k += 1