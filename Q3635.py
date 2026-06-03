# PART OF DAILY LEETCODE PROBLEM
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        land_min = landStartTime[0] + landDuration[0]
        for i in range(1, len(landDuration)):
            land_min = min(land_min, landStartTime[i] + landDuration[i])
        ans = landStartTime[0] + landDuration[0] + waterStartTime[0] + waterDuration[0]
        for i in range(len(waterStartTime)):
            ans = min(ans, max(land_min,waterStartTime[i]) + waterDuration[i])
        
        water_min = waterStartTime[0] + waterDuration[0]
        for i in range(1, len(waterStartTime)):
            water_min = min(water_min, waterStartTime[i] + waterDuration[i])
        for i in range(len(landStartTime)):
            ans = min(ans, max(water_min,landStartTime[i]) + landDuration[i])
    
        return ans 
        