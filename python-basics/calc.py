import argparse

# store history
history = []

parser = argparse.ArgumentParser(
    description="CLI Calculator - Perform basic arithmetic operations"
)

parser.add_argument(
    "operation",
    help="Operation to perform: add, sub, mul, div, history"
)

parser.add_argument(
    "a",
    type=float,
    nargs="?",
    help="First number"
)

parser.add_argument(
    "b",
    type=float,
    nargs="?",
    help="Second number"
)

args = parser.parse_args()

# show history
if args.operation == "history":
    if len(history) == 0:
        print("No calculations yet.")
    else:
        for item in history:
            print(item)

# addition
elif args.operation == "add":
    result = args.a + args.b
    expression = f"{args.a} + {args.b} = {result}"
    history.append(expression)
    print(result)

# subtraction
elif args.operation == "sub":
    result = args.a - args.b
    expression = f"{args.a} - {args.b} = {result}"
    history.append(expression)
    print(result)

# multiplication
elif args.operation == "mul":
    result = args.a * args.b
    expression = f"{args.a} * {args.b} = {result}"
    history.append(expression)
    print(result)

# division
elif args.operation == "div":
    if args.b == 0:
        print("Error: Cannot divide by zero")
    else:
        result = args.a / args.b
        expression = f"{args.a} / {args.b} = {result}"
        history.append(expression)
        print(result)

else:
    print("Invalid operation")