class vowels:

    vowels = 'ayoueiAYOUEI'

    def __init__(self, string):
        self.string = string
        self.i = 0


    def __iter__(self):
        return self

    def __next__(self):

        while self.i < len(self.string):
            if self.string[self.i] in self.vowels:
                break
            self.i += 1


        if self.i >= len(self.string):
            raise StopIteration



        char = self.string[self.i]
        self.i += 1
        return char


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)