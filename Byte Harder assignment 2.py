

def parse_to_dict(file) -> dict:
    with open(file, "r") as f:
        raw_str = f.read()
        new_dict = {}
        split = raw_str.split(":")
        index = 0
        while True:
            try:
                entry = split[index]
                key, value = entry.split(" | ")
                new_dict[key.strip()] = value.strip()
                index += 1
            except IndexError:
                break
    return new_dict


def dict_remove_vowels(my_dict: dict) -> dict:
    forbidden = ["a", "e", "i", "o", "u"]
    for key, value in my_dict.items():
        count = 0
        new_val = ''
        for letter in value:
            if letter in forbidden:
                count += 1
            else:
                new_val += letter
        new_val += str(count)
        my_dict[key] = new_val
    return my_dict


def final():
    for file in ("file_1.txt", "file_2.txt"):
        dict_values = parse_to_dict(file)
        the_dict = dict_remove_vowels(dict_values)
        for key, value in the_dict.items():
            print(f"The value {value[:-1]} for key {key} has {value[-1]} vowels")



final()
