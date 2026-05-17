class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        num = sorted(nums)
        list2 = []
        for i in range(len(num)-1):
            j = i + 1
            k = len(num)-1
            num1 = num[i]
            while j < k:
                if num[j] + num[k] == -(num1):
                    list2.append([num1, num[j], num[k]])
                    j += 1
                    k -= 1
                else:
                    if num[j] + num[k] > -(num1):
                        k -= 1
                    else:
                        j += 1
                    
        list3 = [list(x) for x in set(tuple(x) for x in list2)]
        return list3
