class sequence_repeat:
    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.count <= 0:
            raise StopIteration

        if self.i >= len(self.sequence):
            self.i = 0

        i = self.i
        self.i += 1

        self.count -= 1
        return self.sequence[i]

result = sequence_repeat('abc', 5)
for i in result:
    print(i, end='')




