# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)   
        curr = head          
        carry = 0            
        while l1 is not None and l2 is not None: 
            data = l1.val + l2.val + carry
            if data > 9:
                carry = 1
                data -= 10
            else:
                carry = 0
            curr.next = ListNode(data)  
            curr = curr.next             
            l1 = l1.next
            l2 = l2.next
        while l1 is None and l2 is not None:
            data = l2.val + carry
            if data > 9:
                carry = 1
                data -= 10
            else:
                carry = 0
            curr.next = ListNode(data)
            curr = curr.next
            l2 = l2.next
        while l1 is not None and l2 is None:
            data = l1.val + carry
            if data > 9:
                carry = 1
                data -= 10
            else:
                carry = 0
            curr.next = ListNode(data)
            curr = curr.next
            l1 = l1.next
        if carry == 1:
            curr.next = ListNode(1)
        return head.next