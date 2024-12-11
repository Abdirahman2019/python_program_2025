print("===================================")
print("         welcome to Gender base census    ")
print("===================================")
def Gender():
        male = ["abdirahman","osman","ismail","hassan"]
        female = ["ayan","rahma","nusra","kaltum","kusey"]
        return male  , female
            
def main():
    male, female =Gender()
    while True:
         name = input("Enter your name or Type 'exit' to quit the program: ").strip().lower()
         if name == "exit":
              print("Exiting the program. Goodbye!")
              break
         elif name in male:
            print("your Gender is male")  
         elif name in female:
            print("your gender is female!!")
         else:
              print("The Gender not registered") 
main()            