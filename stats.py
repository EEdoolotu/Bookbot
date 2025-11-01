def get_num_words(book):
    words = book.split()
    return len(words)


def count(text):
    storage = {}
    for char in text:
        new_str = char.lower()
        if new_str in storage:
            storage[new_str] += 1
        else:
            storage[new_str] = 1
        
    return storage


def sort_on(items):
    return items["num"]

    
def sort_it_out(the_dict):
    sorted_list = []
    for ch in the_dict:
        sorted_list.append({"char": ch, "num": the_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
