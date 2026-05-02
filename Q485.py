class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = temp = nums[0]

        for num in nums[1:]:
            if num == 1:
                temp = temp + 1
            else:
                temp = 0
            count = max(count, temp)
        return count
        