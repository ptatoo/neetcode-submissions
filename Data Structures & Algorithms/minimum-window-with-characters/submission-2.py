class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        targetMap = {}
        sMap = {}

        for char in t:
            targetMap[char] = targetMap.get(char, 0) + 1

        l = 0
        r = -1
        output = [0, 1000000]
        has = 0
        need = len(targetMap.keys())

        for r in range(len(s)):
            char1 = s[r]
            if char1 in t: 
                sMap[char1] = sMap.get(char1, 0) + 1
                if sMap[char1] == targetMap[char1]: has += 1
            if has == need:
                while (has == need):
                    char2 = s[l]
                    if char2 in t:
                        sMap[char2] = sMap.get(char2, 1) - 1
                        if sMap[char2] < targetMap[char2]: 
                            has -= 1
                            if (output[1] - output[0]) > (r - l):
                                if (r - l + 1 == len(t)):
                                    return s[l:r + 1]
                                output[0] = l
                                output[1] = r
                    l += 1

        if output[0] == 0 and output[1] == 1000000:
            return ""
        return s[output[0]:(output[1] + 1)]