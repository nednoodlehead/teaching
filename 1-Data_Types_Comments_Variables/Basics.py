
# any line that begins with a # is a commented line
# python will not "read" this and do anything with it. it's entire purpose is for developers to read
# it is good practice to have a space between the hashtag and the beginning of the comment.
# More fomatting best practices can be found at:
# https://peps.python.org/pep-0008/

# variables
# assign a value to a variable using '='
my_variable = 10

# variables store values.


# printing
# you can print values out to the console (also known as stdout, standard output)
print(my_variable)

# printing can be useful for giving feedback to a user or for debugging

# data types
# string. anything inside of "" or '' known as 'str'

my_string = "Hello, this is a string"
my_second_string = 'I can also be single quotes'


# integer. any number (negative, or positive), with no decimal point
my_number = -18
my_second_number = 1991


# float. any number (positive or negative), including a decimal point
my_float = 872.19
my_second_float = -191.10

# complex. an integer followed by the letter j, used in complex math stuffs

my_complex = 1j

# boolean. Either True or False
my_bool_1 = True
my_bool_2 = False


# null / None. Used to represent the absence of a value
my_null = None


# additional content

# anything inside of quotes is a string, no exceptions
i_am_a_string = "19"
i_am_also_a_string = "True"

# there are a few different naming conventions.
# camelCase  (first word starting with lowercase, every word after begins with capital. no underscores)
# snake_case (always lowercase, underscore as a delimeter)
# PascalCase (Every word's first letter is capitalized)
# kebab-case (all lowercase, hyphen as a delimeter)

# python's pep8 naming conventions suggests using snake case for nearly everything. Occasionally PascalCase is used

# to follow general code styling rules, variable names should have no capital letters, and should use underscore '_' as a delimeter


# everything in python is caps sensitive, so `x = true` will throw an error, `x = True` is valid

# python will try it's best to do what you want, but sometimes it is impossible

my_first_num = 10.10  # float
my_alternate_num = 71  # int
# print(my_first_num + my_alternate_num)

my_weird_str = "190"
# print(my_first_num + my_weird_str)
