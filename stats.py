def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars

    
def sort_on(items):
    return items["num"]

def sort_dict(dict):
    char_list = []
    for k, v in dict.items():
        char_list.append({"char": k, "num": v})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list