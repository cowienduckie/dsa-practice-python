from heapq import heappop, heappush


class Solution:
    def clearStars(self, s: str) -> str:
        # Use heap to simulate the problem step by step
        # At each star characters, delete the smallest letter with greatest index
        heap = []
        for i, c in enumerate(s):
            if c == "*":
                if not heap:
                    continue
                heappop(heap)
            else:
                heappush(heap, (c, i * -1))

        # Re-sort the heap by original indices of letters
        heap.sort(key=lambda x: x[1] * -1)

        # Join the charaters for answer string
        return "".join([c for c, _ in heap])
