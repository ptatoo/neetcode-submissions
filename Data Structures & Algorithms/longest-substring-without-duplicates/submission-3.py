class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        result = 0
        length = 0
        prevRepeat = -1

        for i, char in enumerate(s):
            prevRepeat = max(letters.get(char, -1), prevRepeat)
            length = i - prevRepeat
            result = max(result, length)
            letters[char] = i

        return result