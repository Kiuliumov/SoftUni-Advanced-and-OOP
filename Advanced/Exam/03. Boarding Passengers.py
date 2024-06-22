def boarding_passengers(capacity, *args):
    guests_by_benefit = {}
    message = 'Boarding details by benefit plan:\n'
    all_guests = 0
    for group in args:
        all_guests += group[0]

        if capacity == 0:
            break

        number_of_guests, benefit = group

        if number_of_guests > capacity:
            continue

        capacity -= number_of_guests

        if benefit not in guests_by_benefit:
            guests_by_benefit[benefit] = 0

        guests_by_benefit[benefit] += number_of_guests

    sorted_benefits = sorted(guests_by_benefit.items(), key=lambda item: (-item[1], item[0]))
    current_guests = 0

    for benefit, number_of_guests in sorted_benefits:
        current_guests += number_of_guests
        message += '## {}: {} guests\n'.format(benefit, number_of_guests)

    guests_waiting = all_guests - current_guests

    if guests_waiting == 0 and not capacity:
        message += 'All passengers are successfully boarded!'
    elif guests_waiting > 0 and capacity > 0:
        message += 'Partial boarding completed. Available capacity: {}.'.format(capacity)
    else:
        message += 'Boarding unsuccessful. Cruise ship at full capacity.'

    return message

