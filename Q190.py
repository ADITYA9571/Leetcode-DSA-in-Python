class Solution:
    def reverseBits(self, n: int) -> int:
        num1 = n
        bits1 = format(num1, '032b')
        bits2 = bits1[::-1]
        num2 = int(bits2,2)
        return num2