print("Hello World!")

# print function just prints the given data and gives it as an output.
# for every code there is a must output

print("My name is Raj Aryan.", "I'm thriving to become an AI Engineer.")
print("My age is", 20+1, ".")


# declaration of variables:

name = "RAJ ARYAN"
age = 21
place = "Patna"
print(name, age, place)


# Identifiers Rules:    a-z, A-Z, 0-9, _
# 1variable is wrong
thisisapythonvariable = "raj"  # should be simple and short and relatable/meaningful to the value it stores.


# DataTypes: integers, string, float, boolean, none.
print(type(name))           # <class 'str'>
print(type(age))            # <class 'int'>
print(type(25.99))          # <class 'float'>


# integers
x = 25
y = -25
z = 0

# strings
a = 'raj'
b = "raj"      ## preferred
c = '''raj'''
print(a, b, c)


moyemoye = None
oyehoye = True

print(type(moyemoye))          # <class 'NoneType'>     
print(type(oyehoye))           # <class 'bool'>

# comments
# single line comments
"""
multi-line
comment
"""

# implicit conversion
p = 10
q = 23.56
sum = p+q
print(sum)

#explicit conversion
l = 1 
m = "2"
n = int(m)             # <class 'int'>
res = l+n
print(res)  
print(type(n))