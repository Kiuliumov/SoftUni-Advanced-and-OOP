given_words = sorted(input())
set_of_words = set(given_words)
for char in given_words:
    if char in set_of_words:
        print(f'{char}: {given_words.count(char)} time/s')
        set_of_words.remove(char)

