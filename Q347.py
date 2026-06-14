class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] = dict1[num] + 1
        top_keys = sorted(dict1, key=dict1.get, reverse=True)[:k]

        return top_keys