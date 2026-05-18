class Solution:
    def myAtoi(self, s: str) -> int:
        str1 = "0123456789"
        str2 = ""
        flag = 2
        index = 0
        for i, ch in enumerate(s):
            if ch in str1:
                break
            if ch == "-":
                flag = 1
                index = i+1
                break
            elif ch == "+":
                flag = 0
                index = i+1
                break
        for ch in s[index:]:
            if ch == " " and len(str2) == 0 and flag == 2 :
                continue 
            if ch in str1 :
                str2 += ch
            else:
                break 
        if len(str2) == 0:
            return 0
        num1 = int(str2)
        num1 = ((-1)**flag)*(num1)
        if num1 < (-1)*2**31:
            num1 = (-1)*2**31
        elif num1 > 2**31 - 1:
            num1 = 2**31 - 1
        return num1