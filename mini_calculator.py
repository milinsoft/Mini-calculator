# write your code here
import random
import os
import os.path


def choose_level():
    # choosing the difficulty level
    global level
    lvl = input("""Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29\n""")
    if lvl == "1":
        return "1"
    elif lvl == "2":
        return "2"
    else:
        print("Incorrect option chosen, please try again")
        return choose_level()


def calculation(expr):
    # for the level 1 function takes  a sting with a math expression, calculates and returns the answer.
    # possible operations are: addition("+), subtraction("-") and multiplication("*"). Division is not allowed here for now
    # execution if level is 1
    if level == "1":
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
    # execution if level is 2
    else:
        return pow(expr, 2)


def math_task_generator():
    # this function generates math task for 2 levels of difficulty
    # for level 1 random math expression line a +/-/* b is generated, where a&b are in range 2-9
    # for level 2 random number is generated. Range 11-29
    if level == "1":
        arg1 = random.randint(2, 9)
        operator = random.choice("+-*")
        arg2 = random.randint(2, 9)
        return str(arg1) + " " + operator + " " + str(arg2)
    else:
        return random.randint(11, 29)


def user_input_check():
    # this function taking user input and if it's not valid (not int) prints an error message and ask to try again
    # returns user_answer if it's ok
    try:
        user_answer = int(input())
    except ValueError:
        print("Incorrect format.")
        return user_input_check()
    else:
        return user_answer


def result_saver():
    # This function will print the user's result to a file and save if user wants to do so
    # otherwise function will terminate the program
    # p.s. user has no chance for a typo here
    save_option = input("Would you like to save the result? Enter yes or no.")  # reading user's choice
    if save_option.lower() == "yes" or save_option.lower() == "y":  # checking possible options that means "to save"
        # check if the file "results.txt" already exists in a current folder.
        # if no - file needs to be created and overwriting is not allowed, hence variable "mode" is introduced
        if not os.path.exists("results.txt"):
            mode = "w"  # this parameter creates file if does not exit
        else:
            mode = "a"  # this parameter appends text data to the end of existing file
        # asking user for his/her name
        name = input("What is your name?")
        # depending on mode opening/creating the "results.txt" file and writing the results into it.
        with open("results.txt", mode) as f1:
            if level == 1:
                lvl = "1 (simple operations with numbers 2-9)"
            else:
                lvl = "2 (integral squares of 11-29)"
            print(f"{name}: {mark}/5 in level {lvl}", file=f1, flush=True)
            print('The results are saved in "results.txt".')
    # terminate the program if user decided not to save his/her results
    else:
        exit()

level = choose_level()

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
result_saver()
