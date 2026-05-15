class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        num1 = 0
        while temp >= 1:
            if num1 <= -2 ** 31 or num1 >= 2**31 - 1:
                return 0
            num1 = temp % 10 + num1
            num1 = num1 * 10 
            temp = temp // 10
        num1 = num1//10
        if x < 0:
            num1 = num1 * (-1)
        return num1
        