class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            if num in nums[i+1 : i+1+k]:
                return True
        return False