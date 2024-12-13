print("***********************************")
print("          LOGIN                    ")
print("***********************************")
def main_page():
    option=int(input("""Enter Your option:
    1.Register:
    2.Login:
    """))
def welcome_page():
    print("WELCOME PAGE!!!")
def login():
    while True:
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        if username == "admin" and  password == "12345":
            print("You Login successfully")
            welcome_page()
            break
        else:
            print("Wrong Username and password!!!")  
login()   
  
