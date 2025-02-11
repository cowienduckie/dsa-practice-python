class Solution:
    """
    Solution using stack and normal string matching
    """

    def removeOccurrences(self, s: str, part: str) -> str:
        # Use a stack to store the answer string
        stack = []
        for c in s:
            # Push character from s into stack
            stack.append(c)
            # If last stack's elements matched with finding part, pop them
            if len(stack) >= len(part):
                is_match = True
                # Substring matching
                for i in range(len(part)):
                    if stack[i - len(part)] != part[i]:
                        is_match = False
                        break
                # If matching, pop the part from stack
                if is_match:
                    for _ in range(len(part)):
                        stack.pop()
        # Join the stack to form final answer
        return "".join(stack)
