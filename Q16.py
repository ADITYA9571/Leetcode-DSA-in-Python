class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if abs(current - target) < abs(closest - target):
                    closest = current
                if current > target:
                    k -= 1
                elif current < target:
                    j += 1
                else:
                    return current 
        return closest 
                