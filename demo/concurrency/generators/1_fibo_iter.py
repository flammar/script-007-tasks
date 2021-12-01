class FiboIterator:
    def __init__(self, n_max):
        self.n_max = n_max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.n_max:
            raise StopIteration
        self.a = self.b
        self.b = self.a + fib
        return fib


for n in FiboIterator(10):
    print(n)
