class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], idx]
            else:
                hashMap[n] = idx

        return [-1, -1]
        
        # hashIdx = {}
        # hashMap = {}

        # for idx, n in enumerate(nums):
        #     if n in hashMap:
        #         hashMap[n] += 1
        #     else:
        #         hashMap[n] = 1

        # for idx, n in enumerate(nums):
        #     reverse = target - n
        #     if (n == reverse):
        #         if n in hashMap and hashMap[n] == 2:
        #             indices = [i for i, x in enumerate(nums) if x == n]
        #             return [min(indices[0], indices[1]), max(indices[0], indices[1])]
        #     else:
        #         if n in hashMap and hashMap[n] == 1 and reverse in hashMap and hashMap[reverse] == 1:
        #             idx2 = nums.index(reverse)
        #             return [min(idx, idx2), max(idx, idx2)]
        
        # return [-1, -1]