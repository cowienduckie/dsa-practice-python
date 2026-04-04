class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Because the given encoded text is fit into a matrix with given rows
        # So, simply initialize the encoding matrix
        cols = len(encodedText) // rows
        mat = [[None] * cols for _ in range(rows)]
        # Fill the encoding matrix with the given encoded text
        i = 0
        for r in range(rows):
            for c in range(cols):
                mat[r][c] = encodedText[i]
                i += 1
        # Read the encoding matrix in a diagonal manner to get the decoded text
        decodedText = ""
        for c in range(cols):
            for r in range(rows):
                if r + c >= cols:
                    break
                decodedText += mat[r][r + c]
        # Remove trailing spaces before returning the decoded text
        return decodedText.rstrip()
