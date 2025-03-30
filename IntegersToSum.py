def sum_of_digits(numbers):
    digits_of_all_sum = 0

    while numbers > 0:
        digit = numbers % 10
        digits_of_all_sum += digit
        numbers //= 10  # Remove the last digit to prevent infinite loop :)

    return digits_of_all_sum


def main():
    num = int(input("Enter an integer: "))
    result = sum_of_digits(num)
    print(f"The sum of the digits of {num} is: {result}")


main()
