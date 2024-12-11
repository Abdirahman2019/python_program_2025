# This code Test if the name type is male or female based on define list.
print("===================================")
print("  welcome to Gender base census    ")
print("===================================")
def Gender():
        male = ["kaka","kamute","mudna","afweyl"]
        female = ["ugas","jimma","mudee","mukulal","mire"]
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
