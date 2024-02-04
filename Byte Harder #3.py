

# not in
#
# my_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# my_str = "hello1!!, thi0193s is 128371a fun 182te18s01t"
#
# new_str = ''
#
# for letter in my_str:
#     if letter not in my_list:
#         new_str += letter

#
# print(f'old string: {my_str}')
# print(f'new string: {new_str}')


# != and ==

# x = "hello"
# x = "hater"
#
# if x == "hello":
#     print('it equals hello')
# elif x != "bruh":
#     print("it does not equal bruh")

# split() method

# x = "Hey how is it going lilbro"
# print(x.split())

# print(x.split("i"))

# a bit more about indexing:

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(x[3])
# print(x[3:])
# print(x[3:5])
# print(x[:3])
# print(x[:-1])


# importing

# import tkinter
# tkinter.Button()

# will import all classes and functions inside the 'tkinter' namespace
# to access the class "Bruh" you would do: tkinter.Bruh()

# from tkinter import Button, Frame, Label
# Button

# will import the specific class from the file
# accessed with: Bruh()
# this means that importing like this can clutter your namespace, as there is no prefix

# importing as alias

# import tkinter as tk
# tk.Button
# now accessed like: tk.bruh
# makes typing prefixes a bit nicer. many libraries will have suggested / often used aliases (pd for pandas,
# np for numpy...)

# if you have two imports that import something with the same name, you can use an alias to resolve the issue

# opening files


# my_file = open("testing.txt", "r")
# print(my_file)
# print(my_file.read())
# my_file.close()

# context managers
# manage the context of how the file is opened

# with open("testing.txt", "r") as my_file:
#     print(my_file.read())

# what happens to the file outside the indentation?

# print(f'here: {f.read()}')

# kwargs and args
# a way to pass many values into functions and unpack them

# def exam(piece):
#     print(piece)
#
# exam("hello")

# def my_func(param_1, *asd, **forget):
#     for param in asd:
#         print(f'passed into args: {param}')
#     for k_param in forget:
#         print(f'passed into kwargs: {k_param}')
#     print(param_1)
#
#
# my_func("hey", "hows", "it", "going", "lilbro", cum="nut", bruh="lethal")

# they do not need to be called args and kwargs, it is just a common use for it. args and kwargs are reserved keywords

# def my_func(*penis, **pine_tree):
#     for param in penis:
#         print(f'passed into args: {param}')
#     for k_param in pine_tree:
#         print(f'passed into kwargs: {k_param}')

# you can also pass in nothing to a function with either *args or **kwargs, and it will be fine. as long as the required
# params are filled, no error will occur

# vowel replacer assignment. replace all vowels in given strings with "#" or something

# file reading and comprehension assignment

# take the following strings and save them as separate files, you may call them whatever you want
# bruh | hella : cool | kid : nice | view
# simple | win : insane | luca : lose | foreever : perfect | victory
#
# your goal is to turn these key-value pairs into a dictionary, with | separating the key-val and : separating the pair
# after that, create a function to remove all vowels from the values of the dictionary
# place the amount of vowels removed onto the end of the value.
# the function should be able to take as many arguments as necessary
# using the function: "Hello" becomes "hll2"
# assume that every word will have vowels, and no more than 9
# at the end of the function, print out each value pair like: "the value Hll for key bruh has 2 vowels removed
# (assuming the key is 'bruh' and the value is 'Hll2'

# the correct output should be:
"""
The value hl for key bruh has 2 vowels
The value k for key cool has 1 vowels
The value v for key nice has 2 vowels
The value w for key simple has 1 vowels
The value l for key insane has 2 vowels
The value frv for key lose has 4 vowels
The value vctr for key perfect has 2 vowels
"""

