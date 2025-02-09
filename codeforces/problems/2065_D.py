from typing import List


def compute_score(arr: List[int]) -> int:
    score = 0
    memo = [0] * len(arr)
    for i in range(len(arr)):
        memo[i] = arr[i] + memo[i - 1]
        score += memo[i]
    return score


def solve():
    # Extract input
    n, m = map(int, input().split())
    arrays = []
    for _ in range(n):
        arrays.append(list(map(int, input().split())))

    # Sort arrays by score descending
    arrays.sort(key=lambda x: (sum(x), compute_score(x)), reverse=True)

    # Concat the arrays and print the final score
    print(compute_score(sum(arrays, [])))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
