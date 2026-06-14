class Solution:
    def deleteNode(self, node):
        temp = node
        temp.val = temp.next.val
        temp.next = temp.next.next