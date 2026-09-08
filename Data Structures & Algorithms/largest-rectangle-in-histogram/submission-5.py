class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Stores (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop taller bars because they cannot extend past current index 'i'
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # Current height 'h' can extend left to 'index'

            stack.append((start, h))

        # Check remaining bars extending all the way to the end of the array
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area