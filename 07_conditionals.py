age = 21

if (age>18):
    print("can vote")
else:
    print("can't vote")

light = "yellow"

if(light == "green"):
    print("Go")            # space at start of line of code is indentation. and is very important in python
elif(light == "yellow"):
    print("Wait")
else:
    print("stop")


    # odd or even
num = int(input("Enter a number: "))
if(num%2 == 0):
    print("Even")
else:
    print("Odd")


    # greatest of three num
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if(a>=b and a>=c):
    print(a, "is the greatest number.")
elif(b>=c):
    print(b, "is the greatest number.")
else:
    print(c, "is the greatest number.")

   # multiple of 7 or not
number = int(input("Enter a number: "))
if(number%7 == 0):
    print(number, "is a multiple of 7.")
else:
    print(number, "is not a multiple of 7")