class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if ' ' not in s:
            return len(s)
        str1 = ''
        for ch in s[::-1]:
            if ch != ' ':
                str1 = str1 + ch
            if ch == ' ' and len(str1) != 0:
                return len(str1)
        return len(str1)
