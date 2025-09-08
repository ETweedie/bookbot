from stats import get_word_count, character_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"{get_word_count(text)} words found in the document")
    print(character_count(text))

main()