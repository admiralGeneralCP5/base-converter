def mult_to_ten(num, base):  # converts a number into base 10
    revnum = []
    for i in num:  # reverses the order so that the power for each place matches the index
        revnum.insert(0, int(i))

    values_for_addition = []

    index_counter = 0
    for i in revnum:
        if i == 1:
            value = base**index_counter
            values_for_addition.append(value)
        index_counter += 1

    final = 0

    for value in values_for_addition:
        final += value

    return final


def ten_to_mult(num, base):  # converts from base 10
    number = int(num)
    remainders = []
    div = 1
    while div > 0:
        div = number // base
        mod = number % base
        remainders.insert(0, mod)

        number = div
    result = ""
    for i in remainders:  # turns the list into a string
        result += str(i)
    return result