import random


class RandomizedSet:

    def __init__(self):
        self.values = set()

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        else:
            self.values.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.values:
            self.values.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.values))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
