class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        pre = "IXCM"
        sum1 = 0
        flag = 0
        for i, ch in enumerate(s[:-1]):
            if flag == 1:
                flag =0
                continue 
            if dict1[s[i]] < dict1[s[i+1]] and ch in pre:
                sum1 = sum1 - dict1[s[i]] + dict1[s[i+1]]
                flag = 1
            else:
                sum1 = sum1 + dict1[s[i]] 
        if flag == 1:
            return sum1
        sum1 = sum1 + dict1[s[-1]]
        return sum1