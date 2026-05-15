class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        temp1 = height[i]
        temp2 = height[j]
        area = min(height[i],height[j])*(j-i)
        while i < j:
            if temp1<temp2:
                i = i + 1
            else:
                j = j - 1
            temp1 = height[i]
            temp2 = height[j]
            temp = min(height[i],height[j])*(j-i)
            area = max(area, temp)
        return area 