# error catching with try / except and raise
# when errors get thrown, the programs stops, like if we try to access index 100 of a list with 4 items
# a try except block will watch for the specified errors and do certain code if the error occurs, instead of stopping
# the program

# my_list = [1, 2, 3, 4, 5, 6]
# print(f'index 100 baby!! {my_list[100]}')

# try:
#     my_list = [1, 2, 3, 4, 5, 6]
#     print(f'index 100 baby!! {my_list[100]}')
# except IndexError:
#     print("ah, an index error")
#
# error as an alias

# try:
#     my_list = [1, 2, 3, 4, 5, 6]
#     print(f'index 100 baby!! {my_list[100]}')
# except IndexError as e:
#     print(f"ah, an index error: {e}")

# broad except

# try:
#     my_list = [1, 2, 3, 4, 5, 6]
#     print(f'index 100 baby!! {my_list[100]}')
# except:
#     print("ah, an error of some kind, dunno what it is")

# catching multiple errors

# try:
#     my_list = [0, 2, 3, 4, 5, 6]
#     for item in my_list:
#         print(item / 0)
# except IndexError:
#     print("ah, an error")
# except ZeroDivisionError:
#     print("you cannot do that lilbro")


# or you can do
# except (IndexError, ZeroDivisionError):
#     pass

# you can also raise errors with the 'raise' keyword

# x = int(input("Enter a value below 10: "))
# if x > 10:
#     raise ValueError("You entred the incorrect value!")