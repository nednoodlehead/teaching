
# dictionaries are one of the most useful tools in python

# dictionaries are ordered and mutable

# dictionaries are defined with squiggly brackets, just like a set, but differ in the way that you add items to it

# dictionaries use what are called 'key-value pairs'. Where the key is a unique object type, and the value is anything

# something like a string, for example is a good candidate for a key

my_dict = {
     "my_key!": "my value, associated with the key",
     "also a key": "second key value",
     19: "third key value",
}

# you do not index into a dicitonary the same way you index into a list. You index using the key.

# print(my_dict["my_key!"])

# you can also use the .get() method

# print(my_dict.get("my_key!"))

# you also use a similar syntax to add to the dictionary

my_dict["My new key!"] = "My super cool value!"

# print(my_dict)

# you can modify keys in the same way you add them

my_dict["My new key!"] = 191.10

# you can also use the update() method

# notice what type you pass in
my_dict.update({"My new key!": True})

# print(my_dict)

# delete a key value pair

my_dict.pop("my_key!")

# print(my_dict)

my_dict["example1 key"] = "hi!"
my_dict["another key!"] = "yippie"
my_dict["my super cool key"] = "and a cooler value"

# view all keys:
all_keys = my_dict.keys()

# view all values:
all_values = my_dict.values()

# view both keys and values!
both = my_dict.items()

# print(all_keys, all_values, both, sep="\n")

# these methods above become a lot more powerful and useful once we get to iteration and if statements!

# nested dictionaries

my_inner_dict = {
     "Yo!": "here",
     "Where": "am i?",
     "Inside the": "outside!"
}

my_dict["funny dictionary"] = my_inner_dict

# print(my_dict)

# you can access these items inside the nested dictionary by:

my_inner_value = my_dict["funny dictionary"]["Where"]

# print(my_inner_value)
