def words_in_book(file_contents):
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    return count

def character_count(file_contents):
    count_dict = {}
    coverted = file_contents.lower()
    for c in coverted:
        if c not in count_dict:
            count_dict[c] = 1
        else:
            count_dict[c] += 1
    return count_dict

# I have a dictionary. I need to take each key/value pair in the dictionary
# and turn them into their own dictionary 
# then I need to add them to a list
# once they are in a list, I need to sort them from biggest to smallest 
# by accessing the value - I need to get each value



def sort_on(dict):
    return dict["count"]

def dict_to_list(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

