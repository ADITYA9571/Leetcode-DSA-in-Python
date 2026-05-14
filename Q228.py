class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        list1 = []
        temp1 = 0
        temp2 = 0
        length = len(nums)
        flag = 0
        for i, num in enumerate(nums[:-1]):
            if flag == 0:
                temp1 = num
                flag = 1
            if num == nums[i+1] - 1:
                continue 
            else:
                temp2 = num
                flag = 0
                if temp1 == temp2:
                    list1.append(f"{temp1}")
                else:
                    list1.append(f"{temp1}->{temp2}")
        if nums[-1] != nums[-2]:
            list1.append(f"{nums[-1]}")
        return list1

# list1.append(f"{temp1}->{i-1}")
