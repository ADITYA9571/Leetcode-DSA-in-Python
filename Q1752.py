# part of my daily streak, DAY-5
class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums)== 1 or nums == sorted(nums):
            return True
        limit = 1
        for i, num in enumerate(nums[:-1]):
            if num <= nums[i+1]:
                pass
            else:
                limit -= 1
        if nums[0] < nums[-1]:
                limit -= 1
        if limit >= 0:
            return True
        else:
            return False
