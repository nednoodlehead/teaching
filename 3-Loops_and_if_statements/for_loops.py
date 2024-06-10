
# for loops are one of the most important tools in programming.
# it allows you it iterate over an iterable
# what is a iterable ? ^^^
# an iterable is an object that can return it's members one at a time
# e.g. mylist = [1, 2, 3, 4]  <- iterable with 4 'members'
# or mystring = "hello!:" <- iterable with 6 'members'

mylist = [1,2,3,4]

for item in mylist:  # 'item' is a new variable
    print(item)


# when it the new variable valid?
for x in mylist:
    print(x)
print(f'x outside: {x}')  # captures the last variable

# what about iterating over numbers?
# for num in 10:  # <-- does not work!
#     print(f"yooo: {num}")

for num in range(10):
    print(f"yooo: {num}")


my_items = ["hi", "hey", "hello", "howdy"]
for count, greeting in enumerate(my_items):
    print(f"greeting: {greeting} num: {count}")


# other utilities like break, continue, pass

# break

for x in range(10):
    if x == 5:
        continue
        # break
    print(f"x is {x}")
    
# why do we iterate? what is an example?
# lets say that we are moderating a chatroom, and bob sends a message. We want to make sure that bob only says nice things, so we check his message against our swear filter
banned_words = ["stinky", "meanie", "smelly"]
bobs_message = "You are stinky!"

for banned_word in banned_words:
    if banned_word in bobs_message:
        print(f"uh oh! bob said a banned word!: {banned_word}")


# you have 10 images that are made within the application, you want to save the images according to the numbers
file_name = "my_image"

for number in range(10):
    filename = f"{file_name}_{number}.png"
    print(f"Saving {filename} to drive!")
