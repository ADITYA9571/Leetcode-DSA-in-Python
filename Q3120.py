# PART OF DAILY LEETCODE PROBLEM 
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        str2 = ""
        for ch in word:
            if ch.islower() and ch.upper() in word:
                if ch not in str2:
                    str2 = str2 + ch
        return len(str2)