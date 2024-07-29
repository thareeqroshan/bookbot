def count_words(book_string):
    return len(book_string.split())

def count_characters(text_string):
    char_dict = {}
    for character in text_string:
        # print(character)
        if(character.lower() in char_dict.keys()):
            char_dict[character.lower()] += 1
        else:
            char_dict[character.lower()] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]


def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    word_len = count_words(file_contents)
    char_dict = count_characters(file_contents)
    # char_dict.sort(reverse=True, key=sort_on)
    sorted_char_dict = dict(sorted(char_dict.items()))
    updated_dict = {}
    for key, value in sorted_char_dict.items():
        if key.isalpha():
            updated_dict[key] = value
    # print(updated_dict)

    print("--- Begin report of " + book_path + " ---")
    print(str(word_len) + " words found in the document\n")
    for key, value in updated_dict.items():
        print("The '" + key + "' character was found " + str(value) + " times")
    # for key, value in char_dict.items():
    #     print("The '" + key + "' character was found "+ str(value) +" times")
    print("--- End report ---")
main()