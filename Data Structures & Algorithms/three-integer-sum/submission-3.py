class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0
        for i, n1 in enumerate(nums):
            if i > 0 and n1 == nums[i - 1]: continue
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                n2 = nums[l]
                n3 = nums[r]
                total = n2 + n3 + n1
                if total < 0: l += 1
                elif total > 0: r -= 1
                else:
                    output.append([n1, n2, n3])
                    while (l < len(nums) and nums[l] == n2):
                        l += 1
                    while (r >= 0 and nums[r] == n3):
                        r -= 1

        return output