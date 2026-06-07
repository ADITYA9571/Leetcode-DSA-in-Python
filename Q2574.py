# PART OF DAILY LEETCODE PROBLEMQ
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        left = [0]
        right = [sum(nums)]
        for i, num in enumerate(nums):
            left.append(left[-1]+ num)
            right.append(right[-1]-num)
        del left[-1]
        del right[0]
        ans = []
        for i in range(len(left)):
            ans.append(abs(left[i] - right[i]))
        return ans 