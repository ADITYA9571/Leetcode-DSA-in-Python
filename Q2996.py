class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        temp = nums[0]
        ans = nums[0]
        
        for i in range(0, len(nums)-1):
            if nums[i] + 1 == nums[i + 1]:
                temp = temp + nums[i + 1]
            else:
                break

        ans = max(ans, temp)
            
        while True:
            if ans in nums:
                ans = ans + 1
            else:
                return ans
