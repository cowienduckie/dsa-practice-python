class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dist = 0
        opt = 0
        for move in moves:
            if move == "L":
                dist -= 1
            elif move == "R":
                dist += 1
            else:
                opt += 1

        if dist >= 0:
            return dist + opt
        else:
            return opt - dist
