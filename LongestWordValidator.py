longest_word = "thelongestwordever"  # Constant longest word, had to make it global so why not?


def check_for_longest_word(user_inputted_word):
    if len(user_inputted_word) > len(longest_word):
        print(f"Your word is the most longest word than {longest_word}!")
    else:
        print(f"Your word is not the most longest word than {longest_word}!")


def main():
    inputted_word = input("Enter your word: ")
    check_for_longest_word(inputted_word)


main()
