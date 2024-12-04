class Solution:
    def compressedString(self, word: str) -> str:
        word += " "
        prev_char = word[0]
        cnt = 0
        ans = []

        for curr_char in word:
            if curr_char == prev_char:
                if cnt == 9:
                    ans.append(str(cnt))
                    ans.append(prev_char)

                    cnt = 1
                else:
                    cnt += 1
            else:
                ans.append(str(cnt))
                ans.append(prev_char)

                cnt = 1
                prev_char = curr_char

        return "".join(ans)
