class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stackH = []
        stackI = []
        maxHeight = heights[0]

        for i, h in enumerate(heights):
            start = i
            if h > maxHeight:
                maxHeight = h
            
            while stackH:
                if stackH[-1] > h:
                    stackH.pop()
                    i = stackI.pop()
                else:
                    break
            if not stackH or stackH[-1] < h:
                stackH.append(h)
                stackI.append(i)

            for j in range(len(stackH)):
                minH = min(stackH[j], h)
                length = start - stackI[j] + 1
                if minH * length > maxHeight:
                    maxHeight = minH * length

        return maxHeight
