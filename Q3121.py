# rip runtime
# PART OF DAILY LEETCODE PROBLEM

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        str2 = ""
        blacklist = ""
        for i, ch in enumerate(word):
            if ((ch.isupper() and ch.lower() in word[i:len(word)])) or ch.lower() in blacklist :
                blacklist = blacklist + ch.lower()
                continue
            if ch.isupper() and ch.lower() in word[:i+1]:
                if ch not in str2:
                    str2 = str2 + ch
        return len(str2)