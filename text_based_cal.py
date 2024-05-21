# private variable to store the result
_result = None  

def _is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def _calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return num1 / num2
    elif operator.lower() == 'r':
        return num2 ** (1 / num1)
    elif operator.lower() == 'x':
        return num1 ** num2
    else:
        raise ValueError(f"Invalid operator: {operator}")

def _evaluate_expression(expression):
    # remove whitespace from the expression
    expression = expression.replace(' ', '')

# check for consecutive operators or invalid terms
    if any(expression[i] in '+-*/rRxX' and expression[i + 1] in '+-*/rRxX=' for i in range(len(expression) - 1)):
        raise ValueError("Invalid expression")