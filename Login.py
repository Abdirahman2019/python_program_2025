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
    print("Welcome to the Registration page")
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
  
