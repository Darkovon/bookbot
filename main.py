from stats import words_in_book, character_count, dict_to_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

# Now i have a sorted list of dictionaries.

def clean_list(sorted_list):

    for d in sorted_list:
        letter = d["char"]
        amount = d["count"]
        if letter.isalpha():
            print(f"{letter}: {amount}")


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    word_count = words_in_book(get_book_text(path_to_file))
    characters = character_count(get_book_text(path_to_file))
    sorted_list = dict_to_list(characters)
  #  print(f"{word_count} words found in the document")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    clean_list(sorted_list)
    print("============= END ===============")

main()