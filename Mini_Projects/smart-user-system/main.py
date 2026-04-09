import configure

print("Welcome to", configure.APP_NAME)

name = input("Enter your name: ")
print("Hello,", name)

while True:

    print("\nSelect an option:")
    print("1. Even or Odd Check")
    print("2. Positive / Negative Check")
    print("3. Largest of Two Numbers")
    print("4. Simple Calculator")
    print("5. Login System")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # -------- Even or Odd --------
    if choice == "1":
        num = int(input("Enter number: "))

        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    # -------- Positive / Negative --------
    elif choice == "2":
        num = int(input("Enter number: "))

        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

    # -------- Largest Number --------
    elif choice == "3":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if a > b:
            print("First number is larger")
        elif b > a:
            print("Second number is larger")
        else:
            print("Both are equal")

    # -------- Calculator --------
    elif choice == "4":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid operator")

    # -------- Login System --------
    elif choice == "5":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == configure.USERNAME and password == configure.PASSWORD:
            print("Login Successful")
        else:
            print("Login Failed")

    # -------- Exit --------
    elif choice == configure.EXIT_OPTION:
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Try again.")