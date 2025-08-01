password = input("Enter your password: ")
if len(password) <10:
    print("Password must be at least 10 characters long.")
    print("Please enter a valid password.")
elif len(password) > 10:
    print("password is secure")
elif len(password) == 10:
    print("Password is of minimum length but not secure. Please add more characters for better security.")