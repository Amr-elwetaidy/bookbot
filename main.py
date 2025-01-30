from collections import defaultdict

def count_letters(text):
    text = text.lower()
    letters = defaultdict(int)
    for char in text:
        letters[char] += 1

    return letters


def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()

    words_count = len(file_contents.split())
    letters = count_letters(file_contents)

    print(f"--- Begin report of {file_name} ---")
    print(f"{words_count} words found in the document", end="\n\n")
    for letter, count in letters.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
