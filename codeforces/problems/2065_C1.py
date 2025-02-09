def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    original = [num for num in a]
    transformed = [b[0] - num for num in a]

    for i in range(1, n):
        if original[i] < min(original[i - 1], transformed[i - 1]):
            original[i] = float("inf")
        if transformed[i] < min(original[i - 1], transformed[i - 1]):
            transformed[i] = float("inf")

    print(
        "YES"
        if original[-1] != float("inf") or transformed[-1] != float("inf")
        else "NO"
    )


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
