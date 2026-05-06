class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        count1 = 0
        count2 = 0
        temp2 = headB
        while temp1:
            while temp2:
                if temp1 == temp2:
                    return temp2
                else:
                    temp2 = temp2.next
            temp2 = headB
            temp1 = temp1.next
        return None