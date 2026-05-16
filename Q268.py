class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = max(nums)*(max(nums)+1)
        temp = temp//2
        if min(nums) != 0:
            return 0
        if temp == sum(nums):
            return max(nums)+1
        else:
            return temp - sum(nums)