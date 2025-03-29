def get_len_combined_strings(first_string, second_string):
    combined_strings = first_string + second_string
    return print(f"Total characters when combined: {len(combined_strings)}")


def main():
    string_a = input("Enter your first string: ")
    string_b = input("Enter your second string: ")

    get_len_combined_strings(string_a, string_b)


main()
