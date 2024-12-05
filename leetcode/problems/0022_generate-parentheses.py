from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n = 2 * n
        ans = []

        def make_parentheses(pos: int, s: str, openings: int) -> None:
            if pos == n:
                if openings == 0:
                    nonlocal ans
                    ans.append(s)
                return
            if openings > 0:
                make_parentheses(pos + 1, s + ")", openings - 1)
            if openings < n - pos:
                make_parentheses(pos + 1, s + "(", openings + 1)

        make_parentheses(0, "", 0)
        return ans


print(
    Solution().generateParenthesis(3)
)  # ["((()))","(()())","(())()","()(())","()()()"]
