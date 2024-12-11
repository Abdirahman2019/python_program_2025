#The first 5 numbers of fibonacci sequences.
def fib(n):
    a, b = 0 , 1
    print(a) #the value of 0
    print(b)  #the value of 1
    for i in  range(2, n):
      c = a + b
      a, b = b , c
      print(c)    
fib(5)
