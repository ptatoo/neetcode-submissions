class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            match char:
                case '+':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val1 + val2)
                case '-':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 - val1)
                case '*':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 * val1)
                case '/':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    output = val2 / val1
                    if output < 0:
                        output = math.ceil(output)
                    else: output = math.floor(output)
                    stack.append(output)
                case _:
                    stack.append(int(char))

        return stack.pop()