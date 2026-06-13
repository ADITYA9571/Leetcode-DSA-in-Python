# PART OF DAILY LEETCODE PROBLEM
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        str1 = ""
        for word in words:
            total = 0
            for ch in word:
                temp1 = ord(ch)%97
                total += weights[temp1]
            total %= 26
            temp2 = 26 - total + 96
            char1 = chr(temp2)
            str1 += char1
        return str1