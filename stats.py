# Contains the functions to analyze the text

def get_word_count(file_string):
    words = file_string.split()
    count = 0
    for _ in range(len(words)):
        count += 1
    
    return count