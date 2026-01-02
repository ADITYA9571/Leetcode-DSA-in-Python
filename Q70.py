class Solution:
    def climbStairs(self, n: int) -> int:
    #    dude its a fibonacci series 
        a = 1
        b = 1
        if n < 2:
            return 1 
        for i in range(2,n+1):
            temp = b
            b = a + b
            a = temp
        return b