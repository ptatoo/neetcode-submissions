class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]] * len(height)
        right = [height[len(height) - 1]] * len(height)

        for i, n in enumerate(height):
            if i == 0: continue
            if n > left[i - 1]:
                left[i] = n
            else:
                left[i] = left[i - 1]

        
        for i in range(len(height) - 2, -1, -1):
            n = height[i]
            if n > right[i + 1]:
                right[i] = n
            else:
                right[i] = right[i + 1]

        total = 0

        for i, n in enumerate(height):
            total += max(0, min(left[i], right[i]) - n)

        return total