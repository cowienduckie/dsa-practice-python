class ProductOfNumbers:
    def __init__(self):
        self.arr = [1]
        self.prefix = [1]  # Prefix product of the indices ignoring 0s, inclusively
        self.zeroes = [0]  # Number of 0s in the prefix, inclusively

    def add(self, num: int) -> None:
        self.arr.append(num)
        # If the number is 0, the prefix product is the same but the number of 0s increases
        if num == 0:
            self.prefix.append(self.prefix[-1])
            self.zeroes.append(self.zeroes[-1] + 1)
        # Otherwise, the prefix product is the product of the previous prefix product and the number
        else:
            self.prefix.append(self.prefix[-1] * num)
            self.zeroes.append(self.zeroes[-1])

    def getProduct(self, k: int) -> int:
        n = len(self.prefix) - 1
        # If the number of 0s between 2 boundaries is different, there must be at least 1 zero between them
        # So, the product is 0
        if self.zeroes[n] != self.zeroes[n - k]:
            return 0
        # If the number of 0s between 2 boundaries is the same, the product is the prefix product of the boundaries
        else:
            return self.prefix[n] // self.prefix[n - k]
