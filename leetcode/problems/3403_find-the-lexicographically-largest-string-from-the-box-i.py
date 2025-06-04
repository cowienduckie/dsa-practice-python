class Solution:
    def answerString(self, word: str, num_friends: int) -> str:
        # Base case: if only 1 player, no need to split anything
        if num_friends == 1:
            return word

        # Compute maximum length of a split word
        word_len = len(word)
        max_split_len = word_len - num_friends + 1

        # Iterate through words and compare answer with the longest substring starting at each index
        ans = word[:max_split_len]
        for i in range(1, word_len):
            ans = max(ans, word[i : i + min(max_split_len, word_len - i)])

        return ans
