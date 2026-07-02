#calculator
def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Can't divide by 0")



def main():
    while True:
        print("\nSimple Calculator")
        operation = input("Choose Operation(+, -, /, *, z(exit)): ")
        if operation == "z":
            print("Goodbye")
            break

        try:
            x = int(input("x: "))
            y = int(input("y: "))
        except ValueError:
            print("Must be an index")


        
        if operation == "+":
            print(add(x, y))
        elif operation == "-":
            print(subtract(x,y))
        elif operation == "*":
            print(multiply(x,y))
        elif operation == "/":
            print(divide(x,y))
        else:
            print("Invalid Operation")

if __name__ == "__main__":
    main()