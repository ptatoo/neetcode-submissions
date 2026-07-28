class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sums = 1
        zeros = 0

        for n in nums:
            if n == 0:
                zeros += 1
            else:
                sums *= n

        output = [0] * len(nums)
        if zeros > 1:
            sums = 0

        for i, n in enumerate(nums):
            if n == 0:
                output[i] = sums
            elif zeros == 1:
                output[i] = 0
            else:
                output[i] = sums // n

        return output
