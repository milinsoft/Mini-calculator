# write your code here
import random


def calculation(expr):
    arg1, operator, arg2 = expr.split()
    arg1, arg2 = int(arg1), int(arg2)
    if operator == "+":
        return arg1 + arg2
    elif operator == "-":
        return arg1 - arg2
    elif operator == "*":
        return arg1 * arg2
    else:
        return "Error. Division should be skipped in this stage. Division operand found"


def math_task_generator():
    arg1 = random.randint(2, 9)
    operator = random.choice("+-*")
    arg2 = random.randint(2, 9)
    return str(arg1) + " " + operator + " " + str(arg2)


def user_input_check():
    # this function taking user input and if it's not valid (not int) prints an error message and ask to try again
    # returns user_answer if it's ok
    try:
        user_answer = int(input())
    except:
        print("Incorrect format.")
        return user_input_check()
    else:
        return user_answer



mark = 5

# a user will be given 5 tasks to solve, that's why the loop is created.
for _ in range(5):
    # assigning the result of math_task_generator() to a variable to make sure we compare the same expression, not a new one
    random_expression = math_task_generator()
    # printing the randomly generated expression so user can see it
    print(random_expression)
    # program reads user's answer invoking the user_input_check() function.
    # function gives a possibility to rerun only user input, not the whole loop
    answer = user_input_check()
    # comparing user's answer with the result of computer's calculation and print "Right!" or "Wrong" respectively
    if answer == calculation(random_expression):
        print("Right!")
    else:
        print("Wrong!")
        mark -= 1
print(f"Your mark is {mark}/5.")
