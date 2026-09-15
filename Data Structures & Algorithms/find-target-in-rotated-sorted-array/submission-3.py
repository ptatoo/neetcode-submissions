class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # Left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Target is in left sorted portion
                else:
                    l = m + 1  # Target is in right portion
            # Right half is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Target is in right sorted portion
                else:
                    r = m - 1  # Target is in left portion

        return -1