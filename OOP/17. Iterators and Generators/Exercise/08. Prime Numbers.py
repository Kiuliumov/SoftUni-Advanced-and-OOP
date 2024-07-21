def get_primes(numbers):
    for number in numbers:
        if number == 0 or number == 1:
            continue
        is_prime = True
        for i in range(2, number):
            if number % i == 0 and number != i:
                is_prime = False

        if is_prime:
            yield number

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))