# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        temp = head
        if count - n == 0:
            temp = temp.next
            return temp 
        while count - n > 1:
            temp = temp.next
            count = count - 1
        temp.next = temp.next.next
        return head