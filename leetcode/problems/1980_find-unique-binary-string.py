from typing import List


class Solution:
    """
    Greedy solution
    Given n bits, we can construct 2^n different strings at max.
    Because we can return any correct answer, we can pick 1 answer greedily in 2 following cases:
        - 111..111: string with all bits are 1
        - 000..001: string with all bits are 0 except 1
    Example: n = 4
        - If nums = [0001, 0010, 0100, 1000] then answer is 1111
        - Otherwise, answer is one of [0001, 0010, 0100, 1000]
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # Base case
        if n == 1:
            return "1" if nums[0] == "0" else "0"
        # Generate n possible answers
        answers = {"0" * i + "1" + "0" * (n - i - 1) for i in range(n)}
        for num in nums:
            if num in answers:
                answers.remove(num)
        # If the was no possible answer left, pick the string with all bits are 1
        return list(answers)[0] if answers else "1" * n
