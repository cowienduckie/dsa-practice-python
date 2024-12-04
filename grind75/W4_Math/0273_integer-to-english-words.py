class Solution:
    def __init__(self):
        self.LESS_THAN_TWENTY = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        self.TENS = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        """
        Convert a 32-bit non-negative integer to text
        """
        if num == 0:
            return "Zero"

        text = ""
        for i in range(len(self.THOUSANDS)):
            if num % 1000 != 0:
                text = self.convert_thousand(num % 1000, self.THOUSANDS[i]) + " " + text
            num //= 1000

        return text.strip()

    def convert_thousand(self, num: int, suffix: str) -> str:
        """
        Convert a non-negative number smaller than 1000 to text
        """
        text = ""
        if num >= 100:
            text += self.LESS_THAN_TWENTY[num // 100] + " Hundred "
            num %= 100

        if num >= 20:
            text += self.TENS[num // 10] + " "
            num %= 10

        if num > 0:
            text += self.LESS_THAN_TWENTY[num] + " "

        return text + suffix + ""
