class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = []
        d = []
        for ch in a[::-1]:
            c.append(int(ch))
        for ch in b[::-1]:
            d.append(int(ch))
        if len(a) >= len(b):
            diff = len(a)- len(b)
            maximum = len(a)
            for i in range(diff):
                d.append(0)
        else:
            diff = len(b) - len(a)
            maximum = len(b)
            for i in range(diff):
                c.append(0)
        str1 = ''
        iteration = 0
        temp = 0 
        while iteration <= maximum - 1:
            if c[iteration] == 1 and d[iteration] == 1:
                num = 0 + temp
                str1 = str1 + str(num)
                temp = 1
            elif c[iteration] != d[iteration]:
                if temp == 0:
                    str1 = str1 + '1'
                    temp = 0
                else:
                    str1 = str1 + '0'
                    temp = 1
            else:
                num = 0 + temp
                str1 = str1 + str(num)
                temp = 0
            iteration = iteration + 1
        if temp == 1:
            str1 = str1 + '1'
        new_str = ''
        for ch in str1[::-1]:
            new_str = new_str + str(ch)
        return new_str