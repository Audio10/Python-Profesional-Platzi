import time
from typing import Counter


class FiboIter():

    def __init__(self, max_number=0):
        self.max_number = max_number

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        self.aux = self.n1 + self.n2
        if self.aux <= self.max_number:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
            else:
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
            return self.n2
        else:
            raise StopIteration("Max number passed")


if __name__ == '__main__':
    fibonacci = FiboIter(3)
    for element in fibonacci:
        print(element)
        time.sleep(1)
