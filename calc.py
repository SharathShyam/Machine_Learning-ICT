class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero!"
        return x / y

    def calculate(self, expression):
        try:
            # Splitting the expression into operands and operator
            operands = expression.split()
            x = int(operands[0])
            operator = operands[1]
            y = int(operands[2])

            # Performing the operation based on the operator
            if operator == '+':
                return self.add(x, y)
            elif operator == '-':
                return self.subtract(x, y)
            elif operator == '*':
                return self.multiply(x, y)
            elif operator == '/':
                return self.divide(x, y)
            else:
                return "Error: Invalid operator!"
        except Exception as e:
            # If there's an error during calculation, print the error message
            return "Error: " + str(e)


def main():
    # Creating an instance of the Calculator class
    calculator = Calculator()

    # Prompting the user to input an expression
    expression = input("Enter an expression (e.g., 1 + 2): ")

    # Calling the calculate method of the Calculator instance and printing the result
    result = calculator.calculate(expression)
    print("Result:", result)


# Calling the main function to start the program
if __name__ == "__main__":
    main()
