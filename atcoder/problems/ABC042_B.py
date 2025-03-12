from functools import cmp_to_key


def main():
    n, l = map(int, input().split())
    strings = []
    for _ in range(n):
        strings.append(input())

    def string_cmp(s1: str, s2: str) -> int:
        for i in range(l):
            if s1[i] != s2[i]:
                return ord(s1[i]) - ord(s2[i])
        return 0

    strings.sort(key=cmp_to_key(string_cmp))

    print("".join(strings))


if __name__ == "__main__":
    main()
