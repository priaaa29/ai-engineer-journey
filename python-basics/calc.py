import argparse

parser = argparse.ArgumentParser(
    description="CLI Calculator"
)

parser.add_argument(
    "operation",
    help="The Operation to perform: add, sub, mul, div, history"
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

# addition
if args.operation == "add":
    result = args.a + args.b

# subtraction
elif args.operation == "sub":
    result = args.a - args.b
    print(result)

# multiplication
elif args.operation == "mul":
    result = args.a * args.b
    print(result)

# division
elif args.operation == "div":
    if args.b == 0:
        print("Error: Cannot divide by zero")
    else:
        result = args.a / args.b
        print(result)

else:
    print("Invalid operation")