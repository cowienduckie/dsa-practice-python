from collections import defaultdict


class Solution:
    """
    Solution using sliding window technique
    """

    def _count_at_least_k(self, word: str, k: int) -> int:
        """
        Return number of substrings having at least k consonants and all vowels
        """

        n = len(word)
        vowels = "ueoai"

        # Use a dictionary to store the count of each vowel and consonant
        vowel_cnt = defaultdict(int)
        consonant_cnt = 0

        # Use sliding window automatically move end pointer
        ans = start = 0

        for end in range(n):
            # Add current character
            if word[end] in vowels:
                vowel_cnt[word[end]] += 1
            else:
                consonant_cnt += 1

            # Try to shrink the current window
            while len(vowel_cnt) == 5 and consonant_cnt >= k:
                # If substring [start, end] valid, then every substring [start, end + x] valid
                ans += len(word) - end

                # Move the start pointer
                if word[start] in vowels:
                    vowel_cnt[word[start]] -= 1
                    # Pop the vowel if it reach 0 to stop the loop
                    if vowel_cnt[word[start]] == 0:
                        vowel_cnt.pop(word[start])
                else:
                    consonant_cnt -= 1
                start += 1
        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Find substrings having exactly k consonants and all vowels
        by finding those that having at least k and k + 1
        """

        return self._count_at_least_k(word, k) - self._count_at_least_k(word, k + 1)
