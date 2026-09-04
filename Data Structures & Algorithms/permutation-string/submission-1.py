class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        targetMap = {}
        s2Map = {}

        for char in 'abcdefghijklmnopqrstuvwxyz':
            targetMap[char] = targetMap.get(char, 0)
            s2Map[char] = s2Map.get(char, 0)

        for char in s1:
            targetMap[char] = targetMap.get(char, 0) + 1
        

        for i in range(len(s1)):
            char = s2[i]
            s2Map[char] = s2Map.get(char, 0) + 1

        if s2Map == targetMap: return True

        for i in range(len(s2) - len(s1)):
            char1 = s2[i]
            char2 = s2[i + len(s1)]
            s2Map[char1] = s2Map.get(char1, 1) - 1
            s2Map[char2] = s2Map.get(char2, 0) + 1
            
            if s2Map == targetMap: return True

        return False