# replacing vowels with a '#' (as a function)

def vowel_replacer(val: str) -> str:
    new_str = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letter in val:
        if letter in vowels:
            new_str += "#"
        else:
            new_str += letter
    return new_str


print(vowel_replacer("seriously this is the first thought ever"))
