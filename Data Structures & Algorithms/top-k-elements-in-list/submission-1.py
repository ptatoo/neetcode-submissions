class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            map[n] = 1 + map.get(n, 0)

        buckets = defaultdict(list)

        for num, freq in map.items():
            buckets[freq].append(num)

        output = []

        for i in range(len(nums), -1, -1):
            if k == 0:
                break
            if i not in buckets:
                continue
            else:
                bucketVals = buckets[i]
                output += bucketVals
                k -= len(bucketVals)
        
        return output
