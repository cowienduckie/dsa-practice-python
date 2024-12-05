from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Pre-compute XOR of all sub-arrays that ending at position i
        n = len(arr)
        prefix_xor = [0] * n
        prefix_xor[0] = arr[0]
        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]

        # Loop through all queries to and return the answer
        # If we know B and C = A XOR B, then we could find A = B XOR C
        ans_list = []
        for [l, r] in queries:
            ans = prefix_xor[r] ^ prefix_xor[l] ^ arr[l]
            ans_list.append(ans)

        return ans_list
