class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            head,sep,tail = haystack.partition(needle)
            size = len(head)
            return size
        else:
            return -1