from typing import List


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # If the expression is a single character, return it
        if expression == "t":
            return True
        elif expression == "f":
            return False

        # If the expression is a negation, return the negation of the inner expression
        if expression[0] == "!":
            return not self.parseBoolExpr(expression[2:-1])

        # If the expression is AND or OR, it should be like &(...) or |(...)
        # The sub-expressions are separated by commas but we need to consider nested expressions
        def split_expression(expression: str) -> List[str]:
            sub_expressions = []
            start = 2  # Start of the current sub-expression
            openings = 0  # Number of opening brackets

            for pos in range(2, len(expression) - 1):
                if expression[pos] == "(":
                    openings += 1
                elif expression[pos] == ")":
                    openings -= 1
                elif expression[pos] == "," and not openings:
                    sub_expressions.append(expression[start:pos])
                    start = pos + 1

            return sub_expressions + [expression[start:-1]]

        # If the expression is an AND, return the AND of the inner expressions
        if expression[0] == "&":
            return all(
                self.parseBoolExpr(expr) for expr in split_expression(expression)
            )

        # If the expression is an OR, return the OR of the inner expressions
        if expression[0] == "|":
            return any(
                self.parseBoolExpr(expr) for expr in split_expression(expression)
            )

        return False  # This should never be reached


ans = Solution().parseBoolExpr("|(&(t,f,t),!(t))")  # True
print(ans)
