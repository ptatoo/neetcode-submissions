class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        countingSet = set()

        for n in nums:
            hashSet.add(n)
            countingSet.add(n)

        maxLength = 0
        for s in hashSet:
            if s not in countingSet:
                continue
            countingSet.discard(s)

            val = s + 1
            count = 1
            while val in countingSet:
                countingSet.discard(val)
                count += 1
                val += 1

            val = s - 1
            while val in countingSet:
                countingSet.discard(val)
                count += 1
                val -= 1

            maxLength = max(maxLength, count)

        return maxLength
