class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        nl = nums[l]
        nr = nums[r]

        if (nl < nr):
            while (l < r):
                m = (l + r) // 2
                n = nums[m]
                if n == target: return m
                elif n < target: l = m + 1
                else: r = m - 1
            if nums[l] != target: return -1
            return l

        if target > nl:
            while (l < r):
                m = (l + r) // 2
                n = nums[m]
                if n == target: return m
                if n < nl: r = m - 1
                elif n < target: l = m + 1
                else: r = m - 1
            if nums[l] != target: return -1
            return l

        if target < nl:
            while (l < r):
                m = (l + r) // 2
                n = nums[m]
                if n == target: return m
                if n >= nl: l = m + 1
                elif n < target: l = m + 1
                else: r = m - 1
            if nums[l] != target: return -1
            return l

        return l