def solve():
    singular = input()
    print(singular[:-2] + "i")


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
