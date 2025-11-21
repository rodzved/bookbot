import sys
from stats import (
    get_num_words,
    get_chars_dict,
    sort_dict
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_characters_count = sort_dict(chars_dict)

    print_report(book_path, num_words, sorted_characters_count)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for i in chars_sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

main()