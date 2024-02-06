import json

quiz_to_do = input("Which Quiz would you like to do?\n1. Data Types, Comments, Variables\n2. More Data Types\n3. Loops & if statements\n4. Extra Utilities (1)\n5. Extra Utilities (2)\
                   \n6. Extra Utilities (3)\n7. Functions\n")

num_to_file = {
    "1": "./1 - Data Types, Comments, Variables\\quiz.json",
    "2": "./2 - More Data Types\\quiz.json",
    "3": "./3 - Loops, and if statements\\quiz.json",
    "4": "./4 - Extra Utilities\\quiz_1.json",
    "5": "./4 - Extra Utilities\\quiz_2.json",
    "6": "./4 - Extra Utilities\\quiz_3.json",
    "7": "./5 - Functions\\quiz.json",
}

with open(num_to_file[quiz_to_do]) as file:
    f = file.read()
    raw_json = json.loads(f)

total_questions = len(raw_json["questions"])
correct_user_answers = 0
answer_list = []
incorrect_user_answers = [] # format is: (question, answers, what user answered, correct answer)
correct_answers = raw_json["answers"]
potential_answers = raw_json["potential_answers"]


for count, question in enumerate(raw_json["questions"]):
    print(question)
    print(potential_answers[count])
    answer = int(input("YOUR ANSWER?: "))
    print("\n")
    answer_list.append(answer)


# check if answers are correct
for count_2, user_answer in enumerate(answer_list):
    correct_answer = raw_json["answers"][count_2]
    if user_answer == correct_answer:
        correct_user_answers += 1
    else:
        incorrect_user_answers.append((raw_json["questions"][count_2], potential_answers[count_2], user_answer, correct_answer))

if correct_user_answers == total_questions:
    print("CONGRATS!! YOU GOT EM ALL RIGHT !!")
else:
    print(f"You scored {correct_user_answers} out of {total_questions}\nHere's what you got wrong:")
    input("Ready to review? (Click enter)")
    for question, answer, user_ans, correct_ans in incorrect_user_answers:
        print(question)
        print(answer)
        print(f"You answered: {user_ans}")
        print(f"The correct answer was: {correct_ans}")
        input("Continue?")
        print("\n")



