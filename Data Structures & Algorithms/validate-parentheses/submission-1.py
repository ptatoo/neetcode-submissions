class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        for char in s:
            if char == '(' or char == '{' or char == '[': arr.append(char)
            else:
                if not arr:
                    return False
                top = arr[-1]
                if char == ')' and top != '(': return False
                if char == '}' and top != '{': return False
                if char == ']' and top != '[': return False
                arr.pop()

        return not arr
            
