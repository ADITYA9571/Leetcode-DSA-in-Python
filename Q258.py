class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            str1 = str(num)
            num = 0
            for ch in str1:
                num += int(ch)
        return num