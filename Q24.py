# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp1 = head 
        count = 0
        
        while temp1 != None:
            count += 1
            temp1 = temp1.next
        temp4 = None
        curr = head
        temp1 = head
        head = head.next

        for i in range(count // 2):
            temp2 = temp1
            temp1 = temp1.next
            temp3 = temp1.next
            temp1.next = temp2
            if temp4:
                temp4.next = temp1
            temp4 = temp2
            temp2.next = temp3 
            temp1 = temp3

        return head