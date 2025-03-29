def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = sum(1 for letter in word if letter in vowels)
    return count


def main():
    word = input("Enter a word: ")
    vowel_count = count_vowels(word)
    print(f"The number of vowels in '{word}' is: {vowel_count}")


main()
