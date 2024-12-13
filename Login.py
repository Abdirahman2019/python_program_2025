print("***********************************")
print("          LOGIN                    ")
print("***********************************")
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
  
