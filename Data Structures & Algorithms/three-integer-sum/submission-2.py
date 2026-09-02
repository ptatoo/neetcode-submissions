class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0
        while (i < len(nums)):
            n1 = nums[i]
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                n2 = nums[l]
                n3 = nums[r]
                if (n3 + n2 + n1 == 0):
                    output.append([n1, n2, n3])
                if (n3 + n2 + n1 <= 0):
                    while (l < len(nums) and nums[l] == n2):
                        l += 1
                if (n3 + n2 + n1 >= 0):
                    while (r >= 0 and nums[r] == n3):
                        r -= 1
            while (i < len(nums) and nums[i] == n1):
                i += 1

        return output