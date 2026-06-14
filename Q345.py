class Solution:
    def reverseVowels(self, s: str) -> str:
        str1 = "aeiouAEIOU"
        left = 0
        right = len(s) - 1
        list1 = list(s)
    
        while left < right:
            if list1[left] not in str1:
                left += 1
                continue 
            elif list1[right] not in str1:
                right -= 1
                continue
            else:
                list1[left], list1[right] = list1[right], list1[left]
                left += 1
                right -= 1
        return "".join(list1)