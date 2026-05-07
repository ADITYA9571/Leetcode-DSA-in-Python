class Solution:
    def hammingWeight(self, n: int) -> int:
        bits1 =  format(n, '032b')
        count = 0
        for digit in str(bits1):
            temp = int(digit)
            if temp == 1:
                count = count + 1
        return count 
