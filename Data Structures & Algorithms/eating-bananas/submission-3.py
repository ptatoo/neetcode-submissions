class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = (sum(piles) + h - 1) // h
        r = max(piles)

        while l < r:
            m = (r + l) // 2
            count = 0
            for p in piles:
                count += (p + m - 1) // m
                if count > h:
                    break
            
            if count > h:
                l = m + 1
            else:
                r = m

        return l