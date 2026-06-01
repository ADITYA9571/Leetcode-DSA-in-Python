# PART OF DAILY LEETCODE PROBLEM 
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost)<3:
            return sum(cost)
        cost.sort(reverse=True)
        total = 0
        count = 0
        for num in cost:
            count += 1
            if count % 3 == 0:
                continue
            total += num
        return total