def get_fruit_count(fruit_name):
    return int(input(f"Enter the number of {fruit_name}: "))


def main():
    apples = get_fruit_count("apples")
    oranges = get_fruit_count("oranges")
    lemons = get_fruit_count("lemons")

    # Display the formatted sentence
    print(f"I have {apples} apples, {oranges} oranges, and {lemons} lemons.")


main()
