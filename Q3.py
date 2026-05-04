class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        left = ans = 0
        for right, ch in enumerate(s):
            if ch in dict1 and dict1[ch] >= left:
                left = dict1[ch] + 1
            dict1[ch] = right 
            ans = max(ans, right - left + 1)
        return ans