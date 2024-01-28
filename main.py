def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print()
    char_report(num_letters)
    print("--- End report ---")






def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    book_text = text.lower()
    letter_count = {}
    for letter in book_text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def char_report(text):
    text_list = list(text.items())
    text_list.sort(key=lambda item: item[1], reverse=True)
    for item in text_list:
        print(f"The '{item[0]}' character was found {item[1]} times")


main()


