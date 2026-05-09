class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            temp1 = temp.next
            temp.next = prev
            prev = temp
            temp = temp1
        return prev