class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list1 = [[1]]
        while numRows>1:
            first = 0
            list2 = []
            for nums in list1[-1]: 
                list2.append(first+nums)
                first = nums 
            list2.append(1)
            list1.append(list2)
            numRows = numRows - 1
        return list1