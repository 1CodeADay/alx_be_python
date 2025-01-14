
def perform_operation(num1, num2, operation('add', 'subtract', 'multiply', 'divide')):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
