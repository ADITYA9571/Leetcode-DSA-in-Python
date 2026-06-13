class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        str1 = " ".join(list1[::-1])
        return str1