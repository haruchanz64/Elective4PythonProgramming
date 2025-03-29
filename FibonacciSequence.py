def get_fibonacci_sequence(limit):
    a, b = 0, 1  # First two fibonacci numbers
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b  # Update values


def main():
    get_fibonacci_sequence(50)  # Generate Fibonacci up to 50.


main()
