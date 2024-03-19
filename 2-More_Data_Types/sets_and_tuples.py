
# Tuples
# defined as a collection of objects inside of cicle brackets -> ()

my_tuple = ("my string!", "second string", 1, True, True)

# tuples are immutable, can have duplicate elements, are ordered

# tuples only have 2 built-in functions. Since they are immutable, there is not a whole lot to do with them in terms of manipulation

# how many times the given value appears in the tuple

# print(my_tuple.count("my string!"))

# search for the fist occurance of the given value, return its position (remember that indexes start at 0)
# print(my_tuple.index(1))

# tuple use cases
# tuples might seem useless when you have lists, and if you wanted to, you probably could go through python without using tuples, but they have some
# use cases where they are the best

# returning from a function. we haven't gone over functions, but just know it is some code that may or may not return something. if it does return something,
# a tuple may be a good type to return the values in, and guarentee that there won't be any unexpected behaviour due to the user changing the order of it, or adjusting the values

# another good example, would be to describe a color using RGB values. you could do:
rgb_value = (10, 29, 100)
# since you don't want any more values there, and you wouldn't want the user of the code to accidently swap index 0 & 1 around
# they also take up slightly less space in memory (not that it really matters at all)


# sets
# defined as a collection of objects inside of squiggly brackets -> {}

# sets are unordered, unindexed, and objects inside are unchangeable, but the set is mutable

# so you can remove objects, and add objects, but you cannot change the objects themselves

my_set = {"hello", "how is it", "going!"}

my_set.add("heyyy")

my_set.remove("hello") 

# what will it print out?
# print(my_set)

# removes and returns a random element
# print(my_set.pop())

# it should be noted, that creating an empty set does not in fact, create an empty set.

am_i_a_set = {}
# print(type(am_i_a_set))

# so we can declare an empty set with the `set()` keyword

i_am_a_set = set()

# set use cases
# sets are very obscure, and are not used incredibly often.

# the main use case I see, is casting a list as a set to remove duplicate elements, and casting it back to a set
my_duplicate_list = [1, 1, 1, 2, 4, 6, 7, 7]

temp = set(my_duplicate_list)

my_new_list = list(temp)

# print(my_new_list)

# another use case could be a word filter. Since you don't want to have duplicate elements, and the order of them doesn't really matter
