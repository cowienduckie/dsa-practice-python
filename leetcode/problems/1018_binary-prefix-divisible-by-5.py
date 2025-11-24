class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        remain = 0
        for num in nums:
            remain = (remain * 2 + num) % 5
            ans.append(remain == 0)
        return ans
