def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def get_word_count(file_string):
    words = file_string.split()
    count = 0
    for _ in range(len(words)):
        count += 1
    
    return count

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"{get_word_count(text)} words found in the document")

main()