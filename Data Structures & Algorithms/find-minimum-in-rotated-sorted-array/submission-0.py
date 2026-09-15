class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        nl = nums[l]
        nr = nums[r]
        if nl < nr:
            return nl

        while (l < r):
            m = (l + r) // 2
            nm = nums[m]
            if (nm < nl):
                r = m
            else:
                l = m + 1

        return nums[l]