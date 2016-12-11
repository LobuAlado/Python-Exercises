#Simple calculator using If conditional

option = 0
while option < 1 or option > 4:
    option = int(input("Select an operation:\n1.Sum\n2.Subtraction\n3.Multiplication\n4.Division\n"))
    if option == 1:
        n1 = int(input("Insert a number: "))
        n2 = int(input("Insert another number: "))
        value = n1 + n2
        print("The result of " + str(n1) + " + " + str(n2) + " is ",value)
    elif option == 2:
        n1 = int(input("Insert a number: "))
        n2 = int(input("Insert another number: "))
        value = n1 - n2
        print("The result of " + str(n1) + " - " + str(n2) + " is ", value)
    elif option == 3:
        n1 = int(input("Insert a number: "))
        n2 = int(input("Insert another number: "))
        value = n1 * n2
        print("The result of " + str(n1) + " * " + str(n2) + " is ", value)
    elif option == 3:
        n1 = int(input("Insert a number: "))
        n2 = int(input("Insert another number: "))
        if n1 != 0 and n2 != 0:
            value = n1 / n2
            print("The result of " + str(n1) + " * " + str(n2) + " is ", value)
        else:
            print("Division by zero")
    else:
        print("--Invalid number--")