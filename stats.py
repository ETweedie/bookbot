# Contains the functions to analyze the text
# function to get the word count in the string from the text file
def get_word_count(file_string):
    words = file_string.split()
    count = 0
    for _ in range(len(words)):
        count += 1
    
    return count

# function to get the count of every character in the text file
def character_count(file_text_string):
    characters = {}
    file_string = file_text_string.lower()

    for i in file_string:
        if i not in characters:
            characters[i] = 1
        elif i in characters:
            characters[i] += 1
    
    return characters

# function to order the character dictionary and return it sorted
def sort_dictionary(character_dict):
    sorted_characters = []

    for key, value in character_dict.items():
        char_num = {"char": key, "num": value}
        sorted_characters.append(char_num)
    
    def sort_on(items):
        return items["num"]
    
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
        