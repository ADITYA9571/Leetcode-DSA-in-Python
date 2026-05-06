class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        temp1 = headA
        temp2 = headB

        while temp1 != temp2:

            if temp1:
                temp1 = temp1.next
            else:
                temp1 = headB

            if temp2:
                temp2 = temp2.next
            else:
                temp2 = headA

        return temp1