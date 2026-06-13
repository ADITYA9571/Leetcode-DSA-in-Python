class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        list1 = []
        k %= len(nums)
        while k > 0:
            k -=1
            temp = nums.pop()
            list1.append(temp)
        nums[:] = list1[::-1] + nums
        