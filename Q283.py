class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = len(nums) - 1
        while 0 <= temp:
            if nums[temp] == 0:
                del nums[temp]
                nums.append(0)
            temp -= 1
        