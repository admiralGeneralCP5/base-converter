from functions import *

while True:
    number = input("Enter a number: ")
    base = int(input("What is the base of your number? >>> "))
    final_base = int(input("What base do you want to convert to? >>> "))

    # if base == '2':
    #     num = input("Enter a base 2 number: ")
    #     print(two_to_ten(num))

    if base == 16:
        print("base 16")
    elif base != 10:
        num_in_10 = mult_to_ten(number, base)
        if final_base == 10:
            print(num_in_10)
        #else:
            #ten_to_mult(num_in_10, final_base)
    else:
        print(ten_to_mult(number, final_base))




# if the base != 10: convert to ten
# then convert to another base if necessary

# else: determine wht base it will need to be converted to

# add subscripts to output

# add a verbose option to show work
