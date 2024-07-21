def reverse_text(string):
    i = len(string) - 1
    while i >= 0:
        current_char = string[i]
        i -= 1
        yield current_char


for char in reverse_text("step"):
    print(char, end='')