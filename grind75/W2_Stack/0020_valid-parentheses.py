class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in bracket_dict.keys():
                stack.append(c)
            else:
                if not stack or c != bracket_dict[stack.pop()]:
                    return False

        return len(stack) == 0
