import json

quiz_to_do = input("Which Quiz would you like to do?\n1. Data Types, Comments, Variables\n2. Working with data types\n3. More Data Types\n4. Loops & if statements\n5. Extra Utilities (1)\n6. Extra Utilities (2)\
                   \n7. Extra Utilities (3)\n8. Functions\n")

num_to_file = {
    "1": "./1-Data_Types_Comments_Variables\\quiz.json",
    "2": "./1-Data_Types_Comments_Variables\\quiz_2.json",
    "3": "./2-More_Data_Types\\quiz.json",
    "4": "./3-Loops_and_if_statements\\quiz.json",
    "5": "./4-Extra_Utilities\\quiz_1.json",
    "6": "./4-Extra_Utilities\\quiz_2.json",
    "7": "./4-Extra_Utilities\\quiz_3.json",
    "8": "./5-Functions\\quiz.json",
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



