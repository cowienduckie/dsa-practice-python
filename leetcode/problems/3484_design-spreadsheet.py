from typing import Tuple


class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0] * 26 for _ in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        """
        Set value for a cell
        """

        row, col = self._convert_cell(cell)
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        """
        Set a cell to 0
        """

        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        """
        Get result of the formula
        """

        if len(formula) == 0 or formula[0] != "=":
            return None

        value_1, value_2 = formula[1:].split("+")
        result = 0

        if self._is_cell(value_1):
            row_1, col_1 = self._convert_cell(value_1)
            result += self.sheet[row_1][col_1]
        else:
            result += int(value_1)

        if self._is_cell(value_2):
            row_2, col_2 = self._convert_cell(value_2)
            result += self.sheet[row_2][col_2]
        else:
            result += int(value_2)

        return result

    def _convert_cell(self, cell: str) -> Tuple[int, int]:
        """
        Convert cell from text to row and column
        """

        col = ord(cell[:1]) - ord("A")
        row = int(cell[1:])

        return (row, col)

    def _is_cell(self, value: str) -> bool:
        """
        Check a text is a cell or not
        """

        return len(value) > 0 and ord("A") <= ord(value[0]) <= ord("Z")
