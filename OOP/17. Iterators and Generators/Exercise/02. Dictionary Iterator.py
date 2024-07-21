class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.i >= len(self.dictionary):
            raise StopIteration

        i = self.i
        self.i += 1
        return list(self.dictionary.items())[i]

result = dictionary_iter({'a': 1, 'b': 2, 'c': 3, 'd': 4})
for item in result:
    print(item)