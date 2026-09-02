class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while (i < j):
            n1 = numbers[i]
            n2 = numbers[j]

            if (n1 + n2 == target):
                return [i + 1, j + 1]
            elif (n1 + n2 > target):
                j -= 1
            else:
                i += 1

        return [0, 0]