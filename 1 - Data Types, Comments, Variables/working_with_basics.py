# you can do simple math with complex, int, and float types
print(3 + 10)
# print(13.11 - 6.55)
# print(-10 * 2)  # * = multiplication
# print(100 / 5) # / = division
# print(100 // 6) # 'floor' (division, but forget the remainder)
# print(103 % 25)  # the remainder of the division, 25 fits into 103 4 times, with 3 remaining, so the result is 3
# print(5 ** 9)  # 5 to the power or 9

# type()

# type() is a function that returns what type of data it is.
# print(type("i am a string!"))
# print(type(171))
# print(type(10.10))


# type casting

# type casting is turning one type into another type, for example, if you create a string:
my_string = "190"

# we can create a new variable, that has the content of my_string, but turned into an int

my_converted_string = int(my_string)

# print(my_converted_string)
# print(type(my_converted_string))

# python will try its best to convert, but it will throw an error if it is impossible

# type_that_will_fail = "my cool string"
# new_type = int(type_that_will_fail)

# so the options you have for converting to primitive types are:
int()
str()
float()
complex()  # complexes cannot be converted into another number type..
bool()

# multi-line strings (aka docstrings)

my_long_string = """ everything here is a string!
even this
and this

"""

# len() function

# len() can be used to get the length of (almost) any object.
# print(len(my_long_string))

# string formatting

example = "i am inside the string!"

my_fomatted_string = f"outside {example} outsie!"

print(my_fomatted_string)

# you can also use commas and '+' to format strings

# print("hello!", example)
# notice the difference..
# print("hello!" + example)

# you are also able to call .upper() and .lower() on the strings to turn them uppercase or lowercase

ex = "Hello World!"
# print(ex.lower())
# print(ex.upper())

# .replace() replaces a character with another one

# new = ex.replace("o", "0")
# print(new)


# concatenate strings (add them together)
a = "Hello"
b = "World!"
c = a + b
# print(c)

# how could we add a space between the words?


# escape characters
# a '\' followed by a character. e.g. \"
# the purpose of this is to be interpreted literally by the interpeter. For example:
# passage = "We were called "Vikings", a weird name"  # invalid syntax compliation error
# so what we do instead:
passage = "We were called \"Vikings\", a weird name"

# it is also used to process special characters, such as a newline (\n) or carriage return (\r)
