class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            m = (r + l) // 2
            count = 0
            for p in piles:
                count += math.ceil(p / m)
            
            if count > h:
                l = m + 1
            else:
                r = m

        return l