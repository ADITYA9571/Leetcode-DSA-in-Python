class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        list1 = []
        while True:
            if temp == None:
                return False
            temp = temp.next
            if temp in list1 :
                return True
            if  temp != None: 
                list1.append(temp)
