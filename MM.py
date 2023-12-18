import random as rd

run = True
total_answers = 0
incorrect_answers = 0
correct_answers = 0


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


def addition_problem():
    global total_answers, correct_answers, incorrect_answers
    a = rd.randrange(1, 50)
    b = rd.randrange(1, 50)
    addition_solution = a + b
    student_choice = get_integer_input(f"""
{a} + {b} = """)
    if student_choice == addition_solution:
        print("Correct")
        total_answers += 1
        correct_answers += 1
    else:
        print("Incorrect")
        total_answers += 1
        incorrect_answers += 1


def subtraction_problem():
    global total_answers, correct_answers, incorrect_answers
    a = rd.randrange(1, 100)
    b = a + rd.randrange(1, 50)
    subtraction_solution = b - a
    student_choice = get_integer_input(f"""
{b} - {a} = """)
    if student_choice == subtraction_solution:
        print("Correct")
        total_answers += 1
        correct_answers += 1
    else:
        print("Incorrect")
        total_answers += 1
        incorrect_answers += 1


def multiplication_problem():
    global total_answers, correct_answers, incorrect_answers  # Declare global variables
    a = rd.randrange(1, 10)
    b = rd.randrange(1, 10)
    multiplication_solution = a * b
    student_choice = get_integer_input(f"""
{a} X {b} = """)
    if student_choice == multiplication_solution:
        print("Correct")
        total_answers += 1
        correct_answers += 1
    else:
        print("Incorrect")
        total_answers += 1
        incorrect_answers += 1


def division_problem():
    global total_answers, correct_answers, incorrect_answers
    a = rd.randrange(1, 10)
    b = rd.randrange(1, 10)
    division_solution = a * b
    student_choice = get_integer_input(f"""
{division_solution} ÷ {a} = """)
    if student_choice == b:
        print("Correct")
        total_answers += 1
        correct_answers += 1
    else:
        print("Incorrect")
        total_answers += 1
        incorrect_answers += 1


def end():
    global total_answers, correct_answers, incorrect_answers, addition, subtraction, combination, multiplication, \
        division, both, everything
    print(f"""
    Congratulations! You got
    {correct_answers} out of 10!

    """)
    total_answers = 0
    incorrect_answers = 0
    correct_answers = 0
    next = input("Return to menu")
    if next == "":
        addition = False
        subtraction = False
        combination = False
        multiplication = False
        division = False
        both = False
        everything = False


while run:
    addition = False
    subtraction = False
    combination = False
    multiplication = False
    division = False
    both = False
    everything = False
    print("""
    Hi, Let's study some maths.
    Do you want to do
    
    (A)ddition,
    (S)ubtraction,
    (C)ombination of addition and subtraction,
    
    (M)ultiplication,
    (D)ivision, or
    (B)oth multiplication and division?
    
    (E)verything!

    (Q)uit
    """)

    mathtype = input('> ')
    if mathtype.upper() == "A":
        addition = True
    if mathtype.upper() == "S":
        subtraction = True
    if mathtype.upper() == "C":
        combination = True
    if mathtype.upper() == "M":
        multiplication = True
    if mathtype.upper() == "D":
        division = True
    if mathtype.upper() == "B":
        both = True
    if mathtype.upper() == "E":
        everything = True
    if mathtype.upper() == "Q":
        quit()

    while addition:
        if total_answers < 10:
            addition_problem()
        if total_answers == 10:
            end()
    while subtraction:
        if total_answers < 10:
            subtraction_problem()
        if total_answers == 10:
            end()
    while combination:
        if total_answers < 10:
            selection = rd.randrange(1, 3)
            if selection == 2:
                addition_problem()
            else:
                subtraction_problem()
        if total_answers == 10:
            end()
    while multiplication:
        if total_answers < 10:
            multiplication_problem()
        if total_answers == 10:
            end()
    while division:
        if total_answers < 10:
            division_problem()
        if total_answers == 10:
            end()
    while both:
        if total_answers < 10:
            selection = rd.randrange(1, 3)
            if selection == 2:
                multiplication_problem()
            else:
                division_problem()
        if total_answers == 10:
            end()
    while everything:
        if total_answers < 10:
            selection = rd.randrange(1, 5)
            if selection == 1:
                addition_problem()
            if selection == 2:
                subtraction_problem()
            if selection == 3:
                multiplication_problem()
            else:
                division_problem()
        if total_answers == 10:
            end()
