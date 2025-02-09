def solve():
    s = input()
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            print(1)
            return
    print(len(s))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
