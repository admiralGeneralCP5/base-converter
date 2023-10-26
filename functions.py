def two_to_ten(b2num):
    revnum = []
    for i in b2num:  # reverses the order so that the power for each place matches the index
        revnum.insert(0, int(i))

    print("revnum", revnum)

    values_for_addition = []

    index_counter = 0
    for i in revnum:
        if i == 1:
            value = 2**index_counter
            values_for_addition.append(value)
        index_counter += 1

    final = 0

    for value in values_for_addition:
        final += value

    return final
