
x = [
    {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5},
    {"first": 6, "second": 7, "third": 8, "fourth": 9, "fifth": 10},
    {"first": 11, "second": 12, "third": 13, "fourth": 14, "fifth": 15},
    ]

new_list = []

for dictionary in x:
    for count, value in enumerate(dictionary.values()):
        new_str = str(value)
        try:
            new_list[count] += new_str
        except IndexError:
            new_list.append(new_str)
print(new_list)
