# Text-Based Calculator

This is a simple text-based calculator implemented in Python. It supports basic arithmetic operations, exponentiation, and root calculations. The calculator reads expressions from the user input, evaluates them, and displays the results.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Exponentiation (`^` or `x`)
- Root calculation (`r`)

## Usage

To run the calculator, simply execute the script. You will be prompted to enter an expression, which should include an equal sign (`=`) at the end. The calculator will evaluate the expression and display the result.

### Example Inputs

- `3 + 4 =`
- `10 / 2 =`
- `5 * 3 =`
- `2 x 3 =`
- `9 r 2 =`

### Exiting the Calculator

To exit the calculator, enter `e` or `q`.

## Code Explanation

### Private Variables

- `_result`: Stores the result of the most recent calculation.

### Helper Functions

- `_is_number(value)`: Checks if a given value is a number.
- `_calculate(num1, operator, num2)`: Performs the specified arithmetic operation on two numbers.
- `_evaluate_expression(expression)`: Evaluates a given mathematical expression.

### Main Function

- `run()`: Runs the text-based calculator, handling user input and displaying results.

## Error Handling

The calculator handles various errors, including:

- Division by zero
- Invalid expressions
- Missing or consecutive operators
- Unmatched parentheses

## Running the Script

To run the script, use the following command:

```sh
python calculator.py
