a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
print("what kind of opration would you like to perform?\n press + to add\n press - to subtract\n press * to multiply\n press / to divide")
operation = input("enter the operation: ")
match operation:
    case '+':
        result = a + b
        print(f"The sum is: {result}")
    case '-':
        result = a - b
        print(f"The difference is: {result}")
    case '*':
        result = a * b
        print(f"The product is: {result}")
    case '/':
        if b == 0:
            print("Cannot divide by zero")
        else:
            result = a / b
            print(f"The quotient is: {result}")
    case _:
        print("Invalid operation. Please enter a valid operation.")
        