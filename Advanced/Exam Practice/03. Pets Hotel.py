def accommodate_new_pets(capacity: int, maximum_weight_limit: float, *args) -> str:
    capacity = int(capacity)
    maximum_weight_limit = float(maximum_weight_limit)
    all_pets_accommodated = True
    pet_dict = {}
    for data in args:
        pet_type, pet_weight = data
        if not capacity:
            all_pets_accommodated = False
            break
        if pet_weight > maximum_weight_limit:
            continue
        capacity -= 1
        if pet_type not in pet_dict:
            pet_dict[pet_type] = 0
        pet_dict[pet_type] += 1
    current_keys = list(pet_dict.keys())
    current_keys.sort()
    pet_dict = sorted(pet_dict.items(), key=lambda x: ord(x[0][0]))
    pet_dict = dict(pet_dict)
    final_string = ''
    if all_pets_accommodated:
        final_string += f'All pets are accommodated! Available capacity: {capacity}.'
    else:
        final_string += 'You did not manage to accommodate all pets!'
    final_string += '\n'
    final_string += 'Accommodated pets:'
    final_string += '\n'
    for key, val in pet_dict.items():
        final_string += f'{key}: {val}'
        final_string += '\n'
    return final_string