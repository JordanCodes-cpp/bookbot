import sys
from stats import (
    get_num_words, 
    char_count, 
    dict_sort
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = char_count(text)
    sorted_char = dict_sort(num_char)
    print_report(book_path, num_words, sorted_char)


def print_report(book_path, num_words, sorted_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for dict in sorted_char:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["count"]}")
        else:
            continue
    print(f"============= END ===============")


def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()


main()
