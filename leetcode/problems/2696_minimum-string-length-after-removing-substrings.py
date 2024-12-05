class Solution:
    def minLength(self, s: str) -> int:
        # Remove any AB or CD in the string
        # Because AB or CD dont have any same character
        # So, only need stack to check and remove
        stack = ["0"]
        for char in s:
            if (char == "B" and stack[-1] == "A") or (char == "D" and stack[-1] == "C"):
                stack.pop()
            else:
                stack.append(char)
        return len(stack) - 1
