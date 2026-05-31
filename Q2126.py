class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        temp = mass
        for num  in asteroids:
            if temp >= num:
                temp += num
            else:
                return False
        return True 
        