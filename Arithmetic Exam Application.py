def calculation(expr):
    arg1, op, arg2 = expr.split()
    arg1, arg2 = int(arg1), int(arg2)
    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    elif op == "*":
        return arg1 * arg2
    else:
        return "Error. Division should be skipped in this stage. Division operand found"

expression = input()

print(calculation(expression))
