def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

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
            print("sum=",add(x,y))
        if operation == 2:
            print("difference=",subtract(x,y))
        if operation == 3:
            print("product=",multiply(x,y)) 
        if operation == 4:
            if y == 0:
               while y == 0:
                   print("Error! invalid denominator")
                   y = float(input("Enter new denominator: "))
                   print("quotient =", divide(x,y))
            else:
                print("quotient=",divide(x,y))
    elif operation not in [1,2,3,4,5]:
        print("Invalid operation, Select another operation")
        continue
    if operation == 5:
        print("Exiting calculator....goodbye😔")
        break
