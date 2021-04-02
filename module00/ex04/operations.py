import sys

def print_error(error):
    print(error)
    print("Usage : python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
    return

argc = len(sys.argv)
if (argc > 3):
    print_error("InputError : too many arguments")
else:
    if argc == 1:
        print_error("")
    else:
        if sys.argv[1].isdigit() and sys.argv[2].isdigit():
            print("Sum: " +str(int(sys.argv[1]) + int(sys.argv[2])))
            print("Difference: "+str(int(sys.argv[1]) - int(sys.argv[2])))
            print("Product: "+str(int(sys.argv[1]) * int(sys.argv[2])))
            if int(sys.argv[2]) == 0:
                print("Quotient: ERROR(div by zero)")
                print("Remainder: ERROR(modulo by zero)")
            else:
                print("Quotient: "+str(int(sys.argv[1]) / int(sys.argv[2])))
                print("Remainder :"+str(int(sys.argv[1]) % int(sys.argv[2])))
        else:
            print_error("InputError : only numbers")

