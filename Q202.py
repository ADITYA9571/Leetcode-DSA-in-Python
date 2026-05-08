class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.square_sums(n)

        return n == 1

    def square_sums(self, num1) -> int:
            sum = 0
            for digits in str(num1):
                sum = sum + int(digits)**2
            return sum