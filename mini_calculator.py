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


# assigning the result of math_task_generator() to a variable to make sure we compare the same expression, not a new one
random_expression = math_task_generator()
# printing the randomly generated expression so user can see it
print(random_expression)

# program reads user's answer
user_answer = int(input())

# comparing user's answer with the result of computer's calculation and print "Right!" or "Wrong" respectively
if user_answer == calculation(random_expression):
    print("Right!")
else:
    print("Wrong!")
