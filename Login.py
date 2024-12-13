print("***********************************")
print("          BUXOW COMPANY LIMITED    ")
print("***********************************")

def main_page():
    option = int(input("""Enter Your option:
    1. Register
    2. Login
    """))
    if option == 1:
        Register()
    elif option == 2:
        login()
    else:
        print("Invalid option. Please try again.")
        main_page()

def Register():
    print("***********************************")
    print("   WELCOME TO REGISTRATION PAGE     ")
    print("***********************************")
    Fname = input("Enter Your First Name: ")
    lname = input("Enter Your Last Name: ")
    ID_No = input("Enter Your ID Number: ")
    phone = input("Enter Your Phone Number: ")
    Gender = input("Enter Gender (Male or Female): ")
    username = input("Create a Username: ")
    password = input("Create a Password: ")

    # Save data to db.txt
    with open("db.txt", "a") as file:
        file.write(f"{username},{password},{Fname},{lname},{ID_No},{phone},{Gender}\n")

    print("---------------------------------------")
    print(f"Your name is  {Fname} {lname}\nID-Number {ID_No}\nPhone {phone}\nGender {Gender}")
    print("---------------------------------------")
    print("Registration successful!")
    main_page()

def welcome_page():
    print("WELCOME PAGE!!!")

def login():
    print("***********************************")
    print("          LOGIN                    ")
    print("***********************************")

    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")

    # Read and verify user data from db.txt
    with open("db.txt", "r") as file:
        users = file.readlines()
        for user in users:
            user_details = user.strip().split(",")
            if user_details[0] == username and user_details[1] == password:
                print("You logged in successfully!")
                welcome_page()
                return
    print("Wrong Username and Password!!!")
    main_page()

main_page()
