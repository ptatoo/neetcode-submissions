class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix)
        w = len(matrix[0])
        r = h * w - 1

        while l <= r:
            m = math.floor((r + l) / 2)
            val = matrix[math.floor(m / w)][m % w]
            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        return False