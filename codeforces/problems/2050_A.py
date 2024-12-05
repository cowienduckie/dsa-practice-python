def solve():
    # Input
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]

    # Iterate over the words and count the number of words that can be written.
    ans = 0
    for word in words:
        if len(word) <= m:
            ans += 1
            m -= len(word)
        else:
            break
    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
