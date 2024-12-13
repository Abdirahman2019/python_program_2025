print("***********************************")
print("          BUXOW COMPANY LIMITED    ")
print("***********************************")
def main_page():
    option=int(input("""Enter Your option:
    1.Register:
    2.Login:
    """))
    if option == 1:
        Register()
    elif option == 2:
       login()   
def Register():
    print("***********************************")
    print("   WELCOME TO REGISTRATION PAGE     ")
    print("***********************************")
    Fname=input("Enter Your First Name: ")
    lname=input("Enter Your Last Name: ")
    ID_No=int(input("Enter Your ID Number: "))
    phone=int(input("Enter Your Phone Number: "))
    Gender=input("Enter Gender: Male or Female: ")
    print("---------------------------------------")
    print(f"Your name is  {Fname} {lname}\n Id-Number {ID_No}\n phone {phone}\n  Gender {Gender}")
    print("---------------------------------------")
def welcome_page():
    print("WELCOME PAGE!!!")
def login():
    while True:
        print("***********************************")
        print("          LOGIN                    ")
        print("***********************************")
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        if username == "admin" and  password == "12345":
            print("You Login successfully")
            welcome_page()
            break
        else:
            print("Wrong Username and password!!!")  
    #111login() 
main_page()
  
