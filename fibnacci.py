#The first 5 numbers of fibonacci sequences.
def fib(n):
    a, b = 0 , 1
    print(a)
    print(b)
    for i in  range(2, n):
      c = a + b
      a, b = b , c
      print(c)    
fib(5)
