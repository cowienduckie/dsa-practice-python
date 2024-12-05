def solve():
    arr = list(map(int, list(input())))
    n = len(arr)

    for i in range(n - 1, -1, -1):
        best = arr[i]
        j = i
        for dist in range(1, 9):
            if i + dist < n and arr[i + dist] - dist > best:
                best = arr[i + dist] - dist
                j = i + dist
        arr[i], arr[j] = arr[j] - (j - i), arr[i]

    print("".join(list(map(str, arr))))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
