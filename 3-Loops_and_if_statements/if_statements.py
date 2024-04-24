

# if statements are one of the most powerful tools in python / programming
# it allows you to execute code based on a condition
# it is also important to know that indentation is very important, your code will not run if
# the indentation is in correct

# if statements are made up of 3 parts

if 10 > 2:
     print("10 is larger than 2!")


# if <statement that is either true or false>:
     # code that is executed if the statement is true

# explain gimmick of everything needing to equal true OR false (numbers, strings..)

if not 1 > 2:  # if 1 is NOT larger than 2:
     print("1 is smaller")


if True:
     print("will this print?")

if False:
     print("am i going to print?")

if 1:
     print("!?")

# into to elif

if 10 != 10:
     print("those values are equal!")
elif 10 == 10:
     print("but these are")
     
# an if statement that also has elifs / else's will only execute the FIRST true statement's code

if 10 == 10:
     print("10 is indeed equal to 10")
elif 10 > 9:
     print("10 is also larger than 9") # not printed


# statements
# != not equals
# == equals
# = ASSIGNMENT, not comparison
# < less than
# > greater than
# <= less than or equal to
# >= more than or equal to
# not operator
# and operator:
if 10 == 10 and 11 == 11:
     print("both are equal!")

# if 10 == 10 and 11:
#      print('fail!')

# else operator
if 10 > 12:
     print("larger")
elif 10 > 100:
     print("somehow?")
else:
     print("none of the previous conditions were true")

# you can have as many elifs as you want, but adding multiple else's is not allowed, and multiple if's results
# in strange behaviour

if "hello" == "hello":
     print("they are equal")
if "world" == "world":
     print("also equal values")
# vs

if "hello" == "hello":
     print("they are equal (2)")
elif "world" == "world":
     print("also equal values (2)")

# pass statement
# if statements have to have something, so if you have an if statement with no content, you can use the `pass` statement to avoid getting
# an error

if "" == "":
     pass  # im not sure what I want to do...


# mock assignment (if time)
# ask the user for a number, and tell them if their number is higher, equal to, or lower than 10.

# hints:  use input(), what type does that give you back? A number, or a string? google it if you dont know
#  
