from functions import *
import os

os.system("clear")

while True:
    print('#' * 25)
    number = input("Enter a number: ").upper()
    if str(number).lower() == '$c' or str(number).lower() == 'clear':
        os.system('clear')
        continue

    base = int(input("What is the base of your number? >>> "))
    final_base = int(input("What base do you want to convert to? >>> "))

    if base != 10:
        num_in_10 = mult_to_ten(number, base)
        if final_base == 10:
            answer = num_in_10
        else:
            answer = ten_to_mult(num_in_10, final_base)
    else:
        answer = ten_to_mult(number, final_base)

    sub1 = get_subscript(base)
    sub2 = get_subscript(final_base)
    print(f"{number}{sub1} --> {answer}{sub2}")
    print('')

