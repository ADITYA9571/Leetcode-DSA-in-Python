class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # temp = max(nums)
        i = 0 
        while i <= max(nums):
            if i not in nums:
                break 
            i += 1
        return i