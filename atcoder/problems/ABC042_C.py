def main():
    n, k = map(int, input().split())

    likes = {str(i) for i in range(10)}
    for dislike in input().split():
        likes.remove(dislike)
    likes = list(likes)

    s = str(n)
    ans = ""
    for i in range(len(s)):
        for digit in likes:
            if digit >= s[i]:
                ans += digit
                break
        if ans[i] > s[i]:
            ans += likes[0] * (len(s) - i - 1)
            break
    print(ans)


if __name__ == "__main__":
    main()
