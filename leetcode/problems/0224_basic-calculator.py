from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        expression_stack = []
        for char in s:
            # Skip spaces
            if char == " ":
                continue
            # If a closing bracket is found, pop the expression inside the bracket to compute the result
            elif char == ")":
                # Store the expression inside the bracket
                bracket_stack = []
                while expression_stack[-1] != "(":
                    bracket_stack.append(expression_stack.pop())
                expression_stack.pop()

                # Compute the result and push it back to the stack
                res = self.compute(bracket_stack)
                # If the result is negative, we need to change the sign before the opening bracket
                if res < 0 and expression_stack and expression_stack[-1] in "+-":
                    expression_stack[-1] = "+" if expression_stack[-1] == "-" else "-"
                    expression_stack += list(str(-1 * res))
                else:
                    expression_stack += list(str(res))
            else:
                expression_stack.append(char)

        return self.compute(expression_stack[::-1])

    def compute(self, expression_stack: List[str]) -> int:
        """
        Compute expression stack with only + and - operators
        """
        if not expression_stack:
            return 0

        # Add a + sign at the beginning of the expression if it doesn't start with an operator
        if expression_stack[-1] not in "+-":
            expression_stack.append("+")

        # Pop each number with its sign and compute the result
        ans = 0
        while expression_stack:
            sign = 1 if expression_stack.pop() == "+" else -1
            num = []
            while expression_stack and expression_stack[-1] not in "+-":
                num.append(expression_stack.pop())
            ans += sign * int("".join(num))

        return ans
