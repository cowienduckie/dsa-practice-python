from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict: Dict[int, int] = dict()
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in num_dict:
                return [num_dict[missing], i]
            else:
                num_dict[nums[i]] = i
        return []
