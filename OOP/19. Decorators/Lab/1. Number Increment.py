def number_increment(numbers: list):

    def increase():
        for i in range(0, len(numbers)):
            numbers[i] += 1
        return numbers
    return increase()


print(number_increment([1,2,3]))