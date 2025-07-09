print("welcome to my calculator!")
print("press 1 to add numbers")
print("press 2 to subtract numbers")
print("press 3 to multiply numbers")
print("press 4 to divide numbers")
print("press 5 to quit")

def addition():
    a = float(input("enter your number:"))
    b = float(input("enter your number:"))
    add = a+b
    print(add)

def subtraction():
    c = float(input("enter your number:"))
    d = float(input("enter your number:"))
    sub = c-d
    print(sub)

def multiplication():
    e = float(input("enter your number:"))
    f = float(input("enter your number:"))
    mul = e*f
    print(mul)

def division():
    g = float(input("enter your number:"))
    h = float(input("enter your number:"))
    div = g/h
    print(div)
    

choice = int(input("enter your choice:"))

if choice == 1:
    addition()

if choice == 2:
    subtraction()

if choice == 3:
    multiplication()

if choice == 4:
    division()

if choice == 5:
    print("quitted")
