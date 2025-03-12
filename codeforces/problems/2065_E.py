def generate_binary(a: int, sa: str, b: int, sb: str, k: int) -> None:
    """
    Assume that a is always greater or equal than b
    """

    # If the difference between a and b is greater than k, then it is impossible to generate the string
    if a - b > k:
        return print("-1")

    # Try to fill the string with the greater number first, then the smaller number with k-length as much as possible
    # If the remaining reach 0, then the loop is done
    ans = ""
    while a > 0 or b > 0:
        if a > 0:
            ans += sa * min(a, k)
            a -= min(a, k)
        if b > 0:
            ans += sb * min(b, k)
            b -= min(b, k)
    return print(ans)


def solve():
    n, m, k = map(int, input().split())
    # If k is greater than both n and m, then it is impossible to generate the string
    if k > m and k > n:
        return print("-1")
    # If n is greater than m, put 0 first as the greater number
    if n > m:
        generate_binary(n, "0", m, "1", k)
    else:
        generate_binary(m, "1", n, "0", k)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
