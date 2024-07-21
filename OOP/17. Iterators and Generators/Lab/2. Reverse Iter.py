class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.i = len(self.iterable) - 1


    def __iter__(self):
        return self

    def __next__(self):

        if self.i < 0:
            raise StopIteration

        i = self.i
        self.i -= 1
        return self.iterable[i]



ri = reverse_iter(range(10))
for i in ri:
    print(i)