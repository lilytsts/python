def g ():
    print("I am in function g") // определение функции g

def f ():
    print("I am in function f")//определение функции f
    g()
    print("I am in function f")

print("I am outside of any function")// вызов функции
f()// вызов функции
print("I am outside of any function")// вызов функции 
