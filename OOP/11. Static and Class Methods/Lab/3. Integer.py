class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(int(value))
        return 'value is not a number'

    @classmethod
    def from_roman(cls, value):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for letter in value:
            value = roman_dict[letter]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value

        return cls(result)

    @classmethod
    def from_string(cls, value):
        try:
            if isinstance(value, str):
                return cls(int(value))
            else:
                return 'wrong type'
        except ValueError:
            return 'wrong type'


integer = Integer(1)
print(integer.value)  # Output: 1
