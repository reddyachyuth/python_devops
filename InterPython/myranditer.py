class MyRandomIterator(object):
    def __init__(self, iterable):
        self.indicesReturnedSoFar = set()
        self.iterable = iterable
    
    def __iter__(self):
        return self
    
    def __next__(self):
        import random
        if len(self.indicesReturnedSoFar) == len(self.iterable):
            raise StopIteration
        
        rand = random.randint(0, len(self.iterable) - 1)
        while rand in self.indicesReturnedSoFar:
            rand = random.randint(0, len(self.iterable) - 1)

        self.indicesReturnedSoFar.add(rand)
        return self.iterable[rand]

mri = MyRandomIterator('hello')
for item in mri:
  print(item)
