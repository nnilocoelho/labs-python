# Example 1 - Variables outside of a function
x = "very good"

def myfunc():
  print("Python is " + x)

myfunc()

# Example 2 - Variables inside a function
x = "Happy New Year"

def myfunc():
    x = "Feliz Ano Novo"
    print("2022! " + x)
    
myfunc()

print("2022! " + x)