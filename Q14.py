class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(s) for s in strs)
        while min_length + 1:
            myset = set(strs)
            count = len(myset)
            if count == 1:
                return strs[0]
            strs = [s[:min_length] for s in strs]
            min_length = min_length - 1
        return ""