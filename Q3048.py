class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        setA = set()
        for nums in arr1:
            temp = str(nums)
            for i in range(len(temp)):
                setA.add(temp[:i+1])
        maxi = 0
        for nums in arr2:
            temp = str(nums)
            for i in range(len(temp)):
                if temp[:i+1] in setA:
                    maxi = max(maxi, i+1) 
        return maxi