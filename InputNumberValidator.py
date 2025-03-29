def get_number(number):
    defined_number = 20
    if number < defined_number:
        print(f"The {number} is less than {defined_number}!")
    else:
        print(f"The {number} is greater than {defined_number}!")


def main():
    user_inputted_number = int(input("Enter your number: "))
    get_number(user_inputted_number)


main()
