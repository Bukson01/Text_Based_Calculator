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
    
    # handle parentheses
    while '(' in expression:
        # find the innermost set of parentheses
        start = expression.rfind('(')
        end = expression.find(')', start)
        if end == -1:
            raise ValueError("Invalid expression")

        # evaluate the expression inside the parentheses
        sub_expr = expression[start + 1:end]
        sub_result = _evaluate_expression(sub_expr)

        # replace the parentheses and sub-expression with the result
        expression = expression[:start] + str(sub_result) + expression[end + 1:]
        
    # split the expression into operands and operators
    operands = []
    operators = []
    num = ''
    for char in expression:
        if char in '+-*/rRxX=':
            if num:
                operands.append(float(num))
                num = ''
            operators.append(char)
        else:
            num += char
    operands.append(float(num))

    # calculate the result
    _result = operands[0]
    for i in range(len(operators)):
        _result = _calculate(_result, operators[i], operands[i + 1])

    return _result

def run():
    print("Welcome to the Text-Based Calculator")
    while True:
        try:
            expression = input("Input: ")
            if expression.lower() in ['e', 'q']:
                break
            elif '=' not in expression:
                raise ValueError("Expression must contain an equal sign")
            else:
                expression = expression[:expression.index('=')]
                _result=_evaluate_expression(expression)
                print(f"{expression}= {int(_result) if _result.is_integer() else round(_result, 5)}")
        except Exception as e:
            print(f"Error: {e}")
    print("Thank you for using the Text-Based Calculator")
    
    
if __name__ == '__main__':
    run()