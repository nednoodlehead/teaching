
# index

# indexing refers to a sequence of values:
# values: "cat" | "dog" | "rabbit" | "zebra"
# index:    0       1        2          3
# indexing begins at 0
# the value for index #2 in this case would be "rabbit"

# mutability
# mutable comes from latin `mutabilis`, "changeable" or "to change"
# mutable means you can change it after it has been created, immutable means you cannot

# strings are immutable, for example, you cannot change the second letter in a string, if you wanted to do that, you could create a new string and make the changes you want.
# a few of the data types we are going over are mutable, and some are immutable, it is important to know.


# lists are one of the 4 built-in types that allow us to store multiple pieces of data in one object
# lists are defined by square brackets

my_list = [] 

# you can also initialize your list with data within it. A list can can contain any amount of objects. Each item must be separated by a comma

my_list_with_content = [1, "hi", None, True, 10.2, 2j]

# a list can also be defined using the list keyword

my_new_list = list()

# lists are mutable, allow duplicate elements, and preserve order

# add to a list

my_list_with_content.append("new item!")

# add an item at a certain index

my_list_with_content.insert(0, "first item!")  # place the string "first item!" at the front of the list

# remove from a list

my_list_with_content.pop(0)  # removes the 1st item from the list

# calling pop with no argument will remove the last item.

my_list_with_content.pop()  # also removes the last item from the list

# indexing into a list

item_number_1 = my_list_with_content[0]

# we can also use negative numbers to index into a list

last_item_in_list = my_list_with_content[-1]

# you can also specify the range of indexes you want
# think of the syntax as number : up to, but not including this number

third_to_fifth = my_list_with_content[2:5]

# replace data at index:

my_list_with_content[1] = "new item at index 2"

# clear the list

my_list_with_content.clear()

