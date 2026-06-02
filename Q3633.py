# PART OF DAILY LEETCODE PROBLEM
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        temp = len(landStartTime)
        mini = (landStartTime[0] + landDuration[0] + waterStartTime[0] + waterDuration[0])
        length = len(waterStartTime)
        for i in range(length):
            for j in range(temp):
                num1 = waterStartTime[i]
                num2 = waterDuration[i]
                num3 = landStartTime[j]
                num4 = landDuration[j]
                total = 0
                if num1 < num3:
                    total = num1 + num2
                    if total <=  num3:
                        total = num3 + num4
                    else:
                        total += num4
                elif num1 > num3:
                    total = num3 + num4
                    if total <= num1:
                        total = num1 + num2
                    else:
                        total += num2
                else:
                    total = num3 + num4 + num2
                mini = min(mini, total)
        return mini