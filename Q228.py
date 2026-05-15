class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        list1 = []
        temp1 = 0
        temp2 = 0
        length = len(nums)
        flag = 0
        
        for i, num in enumerate(nums):
            if flag == 0:
                temp1 = num
                flag = 1
            if num != nums[-1] and num == nums[i+1] - 1:
                later = 1
                if num != nums[-2]:
                    continue 
            else:
                later = 0
                temp2 = num
                flag = 0
                if temp1 == temp2:
                    list1.append(f"{temp1}")
                else:
                    list1.append(f"{temp1}->{temp2}")
        return list1