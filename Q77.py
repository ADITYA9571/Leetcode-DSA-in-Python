class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        list1 = list(range(1, n+1))
        nums = len(list1)
        ans = []

        for mask in range(1 << nums):
            subset = []

            for i in range(nums):
                if mask & (1 << i):
                    subset.append(list1[i])
            if len(subset)==k:
                ans.append(subset)

        return ans