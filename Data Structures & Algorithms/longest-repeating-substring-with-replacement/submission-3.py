class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        maxVal = ""
        maxCount = 0
        result = 0

        l = 0
        r = 0
        while (l < len(s) and r < len(s)):
            c = s[r]
            count = hashMap.get(c, 0) + 1
            hashMap[c] = count
            if count > maxCount:
                maxCount = count
                maxVal = c


            length = r - l + 1
            padding = length - maxCount
            if padding <= k:
                if (length > result): result = length
                r += 1
            else:
                c2 = s[l]
                count = hashMap.get(c2, 1)
                hashMap[c2] = count - 1
                l += 1
                r += 1

        return result