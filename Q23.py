# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list2 = []  
        for head in lists:
            current_node = head
            while current_node:
                list2.append(current_node.val)
                current_node = current_node.next
        list2.sort()
        if not list2:
            return None
        dummy = ListNode(0)
        current = dummy
        for item in list2:
            current.next = ListNode(item)
            current = current.next
        return dummy.next