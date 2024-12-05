def solve():
    num = input()
    mod = twos = threes = 0

    for digit in num:
        if digit == "2":
            twos += 1
        elif digit == "3":
            threes += 1
        mod = (mod + int(digit)) % 9

    for two in range(min(9, twos + 1)):
        for three in range(min(3, threes + 1)):
            if (mod + 2 * two + 6 * three) % 9 == 0:
                print("YES")
                return

    print("NO")


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
