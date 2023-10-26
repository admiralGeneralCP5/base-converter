def mult_to_ten(num, base):  # converts a number into base 10
    num_list = list(num)
    if base == 16:
        index_counter = 0
        for i in num_list:
            if i == 'A':
                num_list.pop(index_counter)
                num_list.insert(index_counter, '10')
            elif i == "B":
                num_list.pop(index_counter)
                num_list.insert(index_counter, '11')
            elif i == "C":
                num_list.pop(index_counter)
                num_list.insert(index_counter, '12')
            elif i == "D":
                num_list.pop(index_counter)
                num_list.insert(index_counter, '13')
            elif i == "E":
                num_list.pop(index_counter)
                num_list.insert(index_counter, '14')
            elif i == "F":
                num_list.pop(index_counter)
                num_list.insert(index_counter, '15')
            index_counter += 1
        num = num_list

    revnum = []
    for i in num:  # reverses the order so that the power for each place matches the index
        revnum.insert(0, int(i))

    values_for_addition = []

    index_counter_b = 0
    for i in revnum:
        value = (base**index_counter_b) * i
        values_for_addition.append(value)

        index_counter_b += 1

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

        # print("div", div)
        # print("mod", mod, '\n')

        number = div
    result = ""
    for i in remainders:  # turns the list into a string
        result += str(i)
    return result