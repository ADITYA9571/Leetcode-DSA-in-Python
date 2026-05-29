# PART OF DAILY LEETCODE PROBLEM
class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = nums[0]
        for num in nums:
            str1 = str(num)
            num = 0
            for ch in str1:
                num += int(ch)
            mini = min(mini, num)
        return mini