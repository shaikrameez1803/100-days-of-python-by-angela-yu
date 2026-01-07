from art import logo

# Calculator functions
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


# Dictionary of operations
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    print(logo)

    num_1 = float(input("What is the first number?: "))

    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num_2 = float(input("What is the second number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        response = input(
            f'Type "y" to continue with {answer}, or "n" to start a new calculation: '
        ).lower()

        if response == "y":
            num_1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()
