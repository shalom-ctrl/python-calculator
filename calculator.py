print("This program performs the basic arithmetic operations")
operation=1
while operation != 5:  
    print("Select the arithmetic operation:")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    while True:
        try:
            operation= int(input("Enter the number corresponding to the operation: "))
            break
        except:
            print("Girllll! That was not a number. Try again.")
    if operation in range(1,5):
        print("Enter two numbers: ")
        while True:
            try:
                x= float(input("First number: "))
                break
            except:
                print("Girllll! That was not a number. Try again.")
        while True:
            try:
                y= float(input("Second number: "))
                break
            except:
                print("Girllll! That was not a number. Try again.")
        if operation == 1:
            print("sum=",x+y)
        if operation == 2:
            print("difference=",x-y)
        if operation == 3:
            print("product=",x*y) 
        if operation == 4:
            if y == 0:
               while y == 0:
                   print("Error! invalid denominator")
                   y = float(input("Enter new denominator: "))
                   print("quotient =", x / y)
            else:
                print("quotient=",x/y)
    elif operation not in [1,2,3,4,5]:
        print("Invalid operation, Select another operation")
        continue
    if operation == 5:
        print("Exiting calculator....goodbye😔")
        break
