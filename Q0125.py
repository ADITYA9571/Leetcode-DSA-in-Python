class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = s.lower()
        check = '0123456789abcdefghijklmnopqrstuvwxyz'
        if len(str1)<=1:
            return True
        str2 = ''
        str3 = ''
        for ch in str1:
            if ch in check :
                str3 = str3+ch
        for ch in str1[::-1]:
            if ch in check :
                str2 = str2+ch
        if str2 == str3:
            return True
        return False