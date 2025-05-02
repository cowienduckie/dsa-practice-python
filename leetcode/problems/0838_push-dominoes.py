class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)

        # Initialize the fallen dominoes and time to fall left
        fallen = list(dominoes)
        left_time = [0] * n

        # Simulate dominoes falling left
        for i in range(n - 2, -1, -1):
            if fallen[i] == "." and fallen[i + 1] == "L":
                fallen[i] = "L"
                left_time[i] = left_time[i + 1] + 1
            else:
                left_time[i] = 0

        # Update final answer by simulating dominoes falling right
        timer = 0
        for i in range(1, n):
            # Reset the timer if current domino is start to fall right or previous one not falling right
            # Otherwise, increase the timer and continue to fall
            if fallen[i] == "R" or fallen[i - 1] != "R":
                timer = 0
                continue
            timer += 1

            # If current domino can continue to fall right, update the fallen dominoes
            if fallen[i] == "." or timer < left_time[i]:
                fallen[i] = "R"
            # If current domini is falling left at the same time, mark it stand
            elif timer == left_time[i]:
                fallen[i] = "."

        return "".join(fallen)
