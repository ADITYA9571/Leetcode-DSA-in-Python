class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list1 = []
        for i, num in enumerate(nums):
            if num == target:
                list1.append(i)
            if num > target:
                break
        if len(list1) == 0:
            return [-1, -1]
        if len(list1) != 2:
            list2 = [list1[0], list1[-1]]   
            return list2
        return list1