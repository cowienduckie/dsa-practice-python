from bisect import bisect_left


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    original = [a[0]] * n
    transformed = [b[0] - a[0]] * n

    for i in range(1, n):
        if a[i] < min(original[i - 1], transformed[i - 1]):
            original[i] = float("inf")
        else:
            original[i] = a[i]

        j = bisect_left(b, a[i] + min(original[i - 1], transformed[i - 1]))
        if j == m:
            transformed[i] = float("inf")
        else:
            transformed[i] = b[j] - a[i]

        if original[i] == transformed[i] == float("inf"):
            print("NO")
            return
    print("YES")


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
