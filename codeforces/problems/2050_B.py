def solve():
    # Input
    n = int(input())
    arr = list(map(int, input().split()))

    # Check if the sum of the array is divisible by n.
    if sum(arr) % n != 0:
        print("NO")
        return

    # Calculate the average of the array.
    # Calculate weather average of odd and even indices are equal to zero.
    avg = sum(arr) // n
    odd = even = 0
    for i in range(n):
        if i & 1:
            odd += arr[i] - avg
        else:
            even += arr[i] - avg

    # Check if the number of odd and even differences are equal to zero.
    if odd == 0 and even == 0:
        print("YES")
    else:
        print("NO")


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
