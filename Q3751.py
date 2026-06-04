# PART OF DAILY LEETCODE PROBLEM
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1, num2+1, 1):
            str1 = str(i)
            list1 = [int(x) for x in str(i)]
            if len(list1) < 3:
                continue
            for j in range(1, len(list1) - 1, 1):
                if list1[j-1] < list1[j] and list1[j] > list1[j+1]:
                    count += 1
                elif list1[j-1] > list1[j] and list1[j] < list1[j+1]:
                    count += 1
                else:
                    continue
        return count