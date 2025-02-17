from collections import defaultdict
from typing import Dict, Set


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Count the frequency of each letters in tiles
        freq = defaultdict(int)
        for c in tiles:
            freq[c] += 1
        # Count visited permutations but exclude the initial empty string
        return self.count_seqs("", freq, set()) - 1

    def count_seqs(self, curr: str, freq: Dict[str, int], checked: Set[str]) -> int:
        # Check if current permutation is checked
        if curr in checked:
            return 0
        checked.add(curr)
        # Try to combine current permutation with leftover letters and count the possibilities
        cnt = 1
        for c, f in freq.items():
            if not f:
                continue
            freq[c] -= 1
            cnt += self.count_seqs(curr + c, freq, checked)
            freq[c] += 1
        return cnt
