class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0] 
        counts = {}
        for number in nums:
            if number in counts:
                counts[number]+=1
            else:
                counts[number]=1     
        for keys in counts:
            if counts[keys] == 1:
                return keys 