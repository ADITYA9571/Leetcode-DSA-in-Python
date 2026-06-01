# PART OF DAILY LEETCODE PROBLEM
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        list1 = []
        for i in range(len(A)):
            count = 0
            for j in range(i+1):
                if A[j] in B[0:i+1]:
                    count = count+1
            list1.append(count)
        return list1 
