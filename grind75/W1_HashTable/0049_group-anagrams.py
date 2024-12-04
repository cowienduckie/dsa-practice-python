from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key in group_dict:
                group_dict[key].append(s)
            else:
                group_dict[key] = list([s])

        return group_dict.values()
