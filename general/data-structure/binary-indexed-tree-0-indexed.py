from typing import List


class BinaryIndexedTree:
    """
    Version 0-indexed of Binary Indexed Tree (BIT), also known as Fenwick Tree.
    """

    def __init__(self, size):
        """
        :param int size: The size of the BIT
        """

        self.size = size
        self.tree = [0] * size

    def load_array(self, arr: List[int]) -> None:
        """
        Load the BIT from an array by adding each element to the BIT.
        Time complexity: O(n log n)

        :param List[int] arr: The array to load from
        :return: None
        """
        for i in range(len(arr)):
            self.add(i, arr[i])

    def fast_load_array(self, arr: List[int]) -> None:
        """
        Fast load the BIT from an array using the difference array method.
        Time complexity: O(n)

        :param List[int] arr: The array to load from
        :return: None
        """
        for i in range(len(arr)):
            self.tree[i] += arr[i]
            if (j := i | (i + 1)) < self.size:
                self.tree[j] += self.tree[i]

    def add(self, index: int, delta: int) -> None:
        """
        Add a delta to the BIT at a given index (0-indexed)

        :param int index: The index to add the delta to
        :param int delta: The delta to add
        :return: None
        """
        while index < self.size:
            self.tree[index] += delta
            index |= index + 1

    def sum(self, index: int) -> int:
        """
        Get the sum of the BIT from index 0 to index (inclusive)

        :param int index: The index to get the sum from
        :return: The sum of the BIT from index 0 to index (inclusive)
        """
        result = 0
        while index >= 0:
            result += self.tree[index]
            index = (index & (index + 1)) - 1
        return result

    def range_sum(self, start: int, end: int) -> int:
        """
        Get the sum of the BIT from start to end (inclusive)

        :param int start: The start index
        :param int end: The end index
        :return: The sum of the BIT from start to end (inclusive)
        """
        return self.sum(end) - self.sum(start - 1)
