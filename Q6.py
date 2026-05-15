class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        current = 0
        direction = 1
        if numRows == 1:
            return s
        for ch in s:
            rows[current] += ch
            if current == 0:
                direction = 1
            elif current == numRows - 1:
                direction = -1
            current += direction
        str1 = ""
        for row in rows:
            str1 += row
        return str1