class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        for i, ch in enumerate(s):
            if ch in dict1 and dict1[ch] != t[i]:
                return False
            else:
                dict1[ch] = t[i]
        
        #cross check 
        dict1 = {}
        for i, ch in enumerate(t):
            if ch in dict1 and dict1[ch] != s[i]:
                return False
            else:
                dict1[ch] = s[i]
        return True 