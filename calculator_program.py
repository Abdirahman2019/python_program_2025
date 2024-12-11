#This program is simple calculator
print("========================================")
print("        CALCULATOR PROGRAM              ")
print("========================================\n")

def Multiplication(): #This define the multiplication function
    x = int(input("Enter your First digit: "))
    y = int(input("Enter your Second digit: "))
    re = x * y
    print("Result:", re)
    return re

def Addition(): #This define the Additon function
    x = int(input("Enter your First digit: "))
    y = int(input("Enter your Second digit: "))
    re = x + y
    print("Result:", re)
    return re

def Subtraction():
    x = int(input("Enter your First digit: "))
    y = int(input("Enter your Second digit: "))
    re = x - y
    print("Result:", re)
    return re

def Division():
    x = int(input("Enter your First digit: "))
    y = int(input("Enter your Second digit: "))
    if y == 0:
        print("Division by zero is not allowed!")
        return None
    re = x / y
    print("Result:", re)
    return re

def main():
    while True:
        print(""" CHOICE  YOU WANT TO OPERATE!!!.
               1.----Multiplication----.
               2.----Addition----.
               3.----Subtraction----.
               4.----Division----
               5.----Exit----
               """)
        option = int(input("Enter Your option: "))
        
        if option == 1:
            Multiplication()
        elif option == 2:
            Addition()
        elif option == 3:
            Subtraction()
        elif option == 4:
            Division()
        elif option == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("You made a wrong selection! Please try again.")

main()
