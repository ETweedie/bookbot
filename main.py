from stats import get_word_count, character_count, sort_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        print("============ BOOKBOT ==============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("------------ Word Count ------------")
        print(f"Found {get_word_count(text)} total words ")
        print("------------ Character Count -----------")
        items = sort_dictionary(character_count(text))
        for item in items:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
            else:
                continue
        print("============ END ============")

main()