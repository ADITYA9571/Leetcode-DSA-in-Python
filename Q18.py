# Trying in n ** 2 time complexity 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        list1 = sorted(nums)
        list2 = []
        i = 0 
        j = len(list1) - 1
        while j - i >= 3:
            k = i + 1
            l = j - 1
            while k < l:
                temp = list1[k] + list1[l] + list1[i] + list1[j]
                if temp == target:
                    list2.append([list1[i], list1[j], list1[k], list1[l]])
                    k += 1
                    l -= 1
                else:
                    if temp > target :
                        l -= 1
                    else:
                        k += 1
                if k == l:
                    break
            if list1[i + 1] + list1[j - 1] + list1[i] + list1[j] > target:
                j -= 1
            else:
                i += 1                
        list3 = [list(x) for x in set(tuple(x) for x in list2)]
        return list3