class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits[len(digits)-1] != 9 or len(digits)==1):
            temp = digits[len(digits)-1]
            del digits[len(digits)-1]
            temp = temp + 1
            if temp < 10:
                digits.append(temp) 
            else:
                digits.append(1) 
                digits.append(temp - 10)
        else:
            count = 0
            while(len(digits)>=1 and digits[len(digits)-1] == 9 ):
                del digits[len(digits)-1]
                count = count+1 
            if(len(digits)!=0):
                digits[len(digits)-1] = digits[len(digits)-1] + 1
                for i in range (0, count):
                    digits.append(0)
            else:
                digits.append(1)
                for i in range (0, count):
                    digits.append(0)
        return digits        