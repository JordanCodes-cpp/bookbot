def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    alpha = {}
    for char in text:
        lowered = char.lower()
        if lowered in alpha:
            alpha[lowered] += 1
        else:
            alpha[lowered] = 1
    return alpha

def sort_on(dict):
    return dict["count"]

def  dict_sort(my_dict):
    new_dict_list = []
    for char, count in my_dict.items():
        char_dict = {
            "char": char,
            "count": count
        }
        new_dict_list.append(char_dict)

    new_dict_list.sort(reverse=True, key=sort_on)
    return new_dict_list
