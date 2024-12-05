from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        stack = []
        for token in tokens:
            if token in operators:
                y, x = stack.pop(), stack.pop()
                stack.append(operators[token](x, y))
            else:
                stack.append(int(token))
        return stack[0]
