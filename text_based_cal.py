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