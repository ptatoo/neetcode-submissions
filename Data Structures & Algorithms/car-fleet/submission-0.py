class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = sorted([(p, (target - p) / s) for p, s in zip(position, speed)], reverse=True)

        for (p, t) in cars:
            if not stack or stack[-1] < t:
                stack.append(t)

        

        return len(stack)
