# This code test the factorial of a number,whereby user enter a digit from the keyboard
num = int(input("Enter a number = "))
if num < 0: #check if the number is less than zero,-ve numbers can not be factorized
    print("The factorial can not be zero")
elif num == 0 or num == 1:
    print("The factorial of",num,"is 1 ") 
else:
    factorial = 1    
    for i in range(1, num + 1):
     factorial *= i 
    print(f"The factorial of {num} is {factorial}")   

