# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        str1 = ""
        while temp:
            str1 = str1 + str(temp.val)
            temp = temp.next
        if str1 == str1[::-1]:
            return True
        else:
            return False
