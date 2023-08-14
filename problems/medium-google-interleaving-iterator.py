from typing import List
# from collections.abc import Iterator

class Iterator:    
    def __init__(self, list: List[int]) -> None:
        self.list = list
        self.lastReadLocation = -1

    def hasNext(self):
        return self.lastReadLocation < len(self.list) - 1

    def next(self):
        if self.hasNext():
            self.lastReadLocation += 1
            return self.list[self.lastReadLocation]
        raise KeyError()

class IF:
    def __init__(self, iterators: List[Iterator]) -> None:
        self.iterators = iterators
        self.lastReadIteratorIndex = -1

    def __incrementIterator__(self):
        self.lastReadIteratorIndex  = (self.lastReadIteratorIndex + 1) % len(self.iterators)
    
    def hasNext(self):
        return any(iterator.hasNext() for iterator in self.iterators)

    def next(self):
        self.__incrementIterator__()
        if self.iterators[self.lastReadIteratorIndex].hasNext():
            return self.iterators[self.lastReadIteratorIndex].next()
        for _ in range(len(self.iterators)):
            self.__incrementIterator__()
            if self.iterators[self.lastReadIteratorIndex].hasNext():
                return self.iterators[self.lastReadIteratorIndex].next()
        raise KeyError()


arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7, 8, 9]

# a = iter(arr1)
# b = iter(arr2)
# c = iter(arr3)

a = Iterator(arr1)
b = Iterator(arr2)
c = Iterator(arr3)

interleave = IF([a,b,c])
while interleave.hasNext():
  print(interleave.next())