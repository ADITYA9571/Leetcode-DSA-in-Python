# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp2 = head
        count = 0
        if temp2 == None or temp2.next == None or k == 0:
            return head
        while temp2 != None:
            count += 1    
            temp2 = temp2.next
        temp2 = head
        while temp2.next != None:  
            temp2 = temp2.next
        temp2.next = head
        temp3 = head
        i = 0
        num1 = count - (k%count) - 1
        while i != num1:
            temp3 = temp3.next
            i += 1
        temp4 = temp3.next
        temp3.next = None
        return temp4
        