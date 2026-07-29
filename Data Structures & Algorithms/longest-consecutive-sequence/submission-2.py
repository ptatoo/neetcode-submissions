class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        maxLength = 0
        for s in hashSet:
            if (s - 1) not in hashSet:
                length = 1

                while (s + length) in hashSet:
                    length += 1

                maxLength = max(maxLength, length)

        return maxLength
