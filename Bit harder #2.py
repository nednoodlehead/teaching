
# += and -= operators
# these are shorthand for x = x + <number> or x = x - <number>
# these are commonly used in loops where, for each iteration, you want a variable to change by an amount
# y = 0
# y = y + 1
# is the same as y += 1

# ITERATION !!

# my_list = [1, 2, 3, 4, 5, 6]
#
# for my_iterable_value in my_list:
#     print(my_iterable_value)


# keeping count of iteration inside for loop
# count = 0
# for my_item in my_list:
#   print("count:", count, "my_item:", my_item)
#   count += 1


# while loops
# great for having multiple conditions that could end the loop
# can use it to access indexes by using a variable that is incremented each loop

# x = 10
# while x < 20:
#     print(f'x is equal to: {x}')
#     x += 1

# using while True:

# x = 10
# while True:
#     print("this will run until a break it hit", x)
#     if x == 30:
#         break
#     x += 1

# better for loops

# unpacking multiple values

# my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# for num_1, num_2 in my_list:
#     print(f"odds: {num_1}, evens: {num_2}")

# you can also access the index of each tuple instead of unpacking inside the for loop

# my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# for my_tuple in my_list:
#     print(f'odds: {my_tuple[0]}, evens: {my_tuple[1]}')

# using enumerate() on a for loop

# my_list = ["Hello", "Hi", "Heya", "Hiya", "Hewwo"]
#
# for count, greeting in enumerate(my_list):
#     print(f"{greeting} is at index {count}")

# unpacking dictionaries with for loops
#
# my_dict = {
#     "Ned": 2,
#     "Hobbes": 3,
#     "Beaned_Benno": 4,
#     "Salad": 5,
#     "Refrain": 6
# }

# for key, value in my_dict.items():
#     print(f'key: {key}, value: {value}')

# will run with an error

# for a_value in my_dict:
#     print(f'value: {a_value}')

# so how do we access the key value pairs?

# for key, value in my_dict.values():
#     print(f'key: {key}, value: {value}')

# how about just the values or keys?

# for x in my_dict.keys()
# for x in my_dict.values()

# using enumerate and dictionary.items() to unpack as expected

# my_dict = {
#     "Ned": 2,
#     "Hobbes": 3,
#     "Beaned_Benno": 4,
#     "Salad": 5,
#     "Refrain": 6
# }

# this should work right?

# for count, (key, value) in enumerate(my_dict.items()):
#     print(f'index of {key} and {value} is {count}')

# this does not work because when we are passing my_dict.items() we are passing in a tuple to the enumerate function.
# the enumerate function returns: <count> and <values>, and values in this case is our tuple (key and value)
# so we can fix it like this:

# for count, (key, value) in enumerate(my_dict.items()):
#     print(f'index of {key} and {value} is {count}')

# or like this:

# for count, key_and_value in enumerate(my_dict.items()):
#     print(f'index of {key_and_value[0]} and {key_and_value[1]} is {count}')

# using continue in a list
# if you are going over a for loop, and you don't care for the current item, you can skip to the next one

# my_list = ["One", "two", None, "three", None, "four", None, None, "five"]
# for entry in my_list:
#     if entry is None:
#         continue
#     print(entry)

# testing time

# given a list of nested dictionaries like: [
# {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5},
# {"first": 6, "second": 7, "third": 8, "fourth": 9, "fifth": 10},
# {"first": 11, "second": 12, "third": 13, "fourth": 14, "fifth": 15},
# ]
# loop through each dictionary
# convert the value for each key-value pair to a string.
# for each one, you need to add the values together, in order. And add the values to a new list (in order).
# so the first entry in this dictionary should be "1611" (which is adding the strings of first in each dict)


