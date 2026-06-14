# PART OF DAILY LEETCODE PROBLEM
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        list1 = []
        while temp:
            list1.append(temp.val)
            temp = temp.next
        i = 0
        j = len(list1) - 1
        maxvalue = list1[i] + list1[j]
        while j >= i + 1:
            maxvalue = max(maxvalue,list1[i] + list1[j])
            i += 1
            j -= 1
        return maxvalue