class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            val = temperatures[i]
            while stack:
                topVal = temperatures[stack[-1]]
                if topVal > val:
                    result[i] = stack[-1] - i
                    stack.append(i)
                    break
                else:
                    stack.pop()
            if not stack:
                stack.append(i)

        return result
            