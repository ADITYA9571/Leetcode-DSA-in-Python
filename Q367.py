class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            if num == mid**2:
                return True
            elif num > mid ** 2:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

