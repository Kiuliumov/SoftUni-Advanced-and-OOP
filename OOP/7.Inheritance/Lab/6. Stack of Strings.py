class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return_str = '[' + ', '.join(item for item in reversed(self.data)) + ']'
        return return_str

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if not self.data:
            return True
        else:
            return False
