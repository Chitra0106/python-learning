#that will take arguments from the command line
import argparse

parser = argparse.ArgumentParser(description='Simple calculator')
parser.add_argument("num1", type=float, help="Number1")
parser.add_argument("num2",type=float, help="Number2")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")
args = parser.parse_args()
#print(args.number)
if args.operation =="add":
    print(args.num1 + args.num2)
elif args.operation =="sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
elif args.operation == "div":
    print(args.num1 / args.num2)
else:
    print("Invalid operation")