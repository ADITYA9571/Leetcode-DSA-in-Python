class Solution:
    def countBits(self, n: int) -> List[int]:
        list1 = []
        for i in range(n+1):
            temp = bin(i)[2:]
            count = 0
            for ch in temp:
                if ch == "1":
                    count += 1
            list1.append(count)
        return list1