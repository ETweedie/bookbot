from stats import get_word_count, character_count, sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    print("============ BOOKBOT ==============")
    print("Analyzing book found at books/frankenstein.txt")
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