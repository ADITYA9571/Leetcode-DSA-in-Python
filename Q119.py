class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = rowIndex
        list1 = [[1]]
        while rowIndex>0:
            first = 0
            list2 = []
            for nums in list1[-1]: 
                list2.append(first+nums)
                first = nums 
            list2.append(1)
            list1.append(list2)
            rowIndex = rowIndex - 1
        return list1[temp]