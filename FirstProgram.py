"""
print("SubhashSushil")
print("Subhash""Sushil")
print("Subhash.", "Sushil.")
print(8001)
print(121 + 874 - 500)

name = "Sushil Kumar Thakur"
age = 24
pricerate = 55.12

print(name, age, pricerate)

print("my name is ", name)

name1 = name,age
print(name1)

# variable check data type
print(type(name))
print(type(age))
print(type(pricerate))

age = 45
old = True
a = None
print(type(age))
print(type(old))
print(type(a))

# Two number prints

a = 500
b = 100
sum = a + b
sub = a - b
mul = a * b
div = a / b
print(sum ,sub, mul,div)


#Operators
# 1. Arithmetics Operator
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b

# 2. Relational Operators return in boolean value(True & False)
a = 50
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
"""

# 3. Assignment Operators
# num = 50
# num = num + 50
# print(num)

# num1 = 100
# num1 += 100
# print(num1)

# num2 = 100
# num2 -= 100
# print(num2)

# num3 = 100
# num3 *= 100
# print(num3)

# num4 = 100
# num4 /=50
# print(num4)

# num5 = 100
# num5 %= 50
# print(num5)

# num6 = 100
# num6 **= 50
# print(num6)

# 4. Logical Operators (ye boolean value ke uppar work karta hain)
# print(not True)
# print(not False)

# a = 50
# b = 20
# print("Not operator:",not a > b)  #(Not operator jab hame koi data  true hai use false karna hain to ye operator use karenge)

# val1 = True
# val2 = True
# print("And operator:", val1 and val2) #(And operator jab dono ka data same ho tab hi true return karega na to false hi return karega)

# val3 = True
# val4 = False
# print("Or operator:", val3 or val4) #(Jab dono me koi ek bhi sahi ho to true retur karega)

# Type Conversion (int, string,float)

"""
convertion = int("5")
convertion = float(5)
convertion = 7775
convertion = str(convertion)
"""
# a = 2
# b = 20.5
# print(type(a + b))
# print(a + b) #Automatically convertion

# c = int("2")
# d = 20.5
# print(type(a + b))
# print(a + b)   #Manually Convartion

# Input in Python

#input("Enter Your Name :")

# name = input("Please enter your name: ")
# print("Welcome ", name)

# val = input("enter your name:")
# print(type(val), val)

# val = int(input("enter your number:"))
# print(type(val), val)

# val = float(input("please enter your number:"))
# print(type(val), val)

# name = input("Please enter your name:")
# age = int(input("Please enter your age:"))
# marks = float(input("please enter your marks:"))

# print("Name = ", name)
# print("Age = ", age)
# print("Marks = ", marks)

# Q. Write a Program to input 2 numbers & Print their Sum.

# first = int(input("enter first number:"))
# second = int(input("enter second number:"))
# print("Sum = ", first + second)

# Q. Write a Program to input side of a square & Print its area.

# side = float(input("Please enter square Side:"))
# print("Area = ", side * side)
# print("Area = ", side ** 2)

# Q. WAP to input 2 floating point number & Print their average.

# a = float(input("enter first:"))
# b = float(input("enter second:"))
# print("Average = ", (a+b)/2)

# Q. WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.

# a = int(input("enter first number:"))
# b = int(input("enter your second number:"))
# print( a >= b)