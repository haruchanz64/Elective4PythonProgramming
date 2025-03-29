def get_sum_of_two_numbers(first_number, second_number):
    sum_of_two_numbers = first_number + second_number
    return sum_of_two_numbers


def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    sum_of_two = get_sum_of_two_numbers(first_number, second_number)
    print(f"The sum of {first_number} and {second_number} is {sum_of_two}.")


main()
