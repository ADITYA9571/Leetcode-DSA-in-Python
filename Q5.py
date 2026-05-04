class Solution:
    def longestPalindrome(self, s: str) -> str:
        str2 = ""
        ans = ""
        if len(s) <= 1:
            return s
        for i in range(len(s)):
            k = len(s)
            while k >= i :
                str2 = s[i:k]
                if self.ispalindrome(str2) and len(str2)>=len(ans):
                    ans = str2
                k = k - 1
        return ans 

    def ispalindrome(self, str1: str) -> bool:
        return str1 == str1[::-1]