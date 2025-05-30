# Exception Handling
a = int(input("Enter a number: "))
b = int(input("Enter 2nd number: "))
try:
    print(a/b)                          # try block encloses the statements that's probable to throw an error in any condition
except:                                 # try block must be followed by an except block
    print("Number can't be divided by zero.")
print("Well Done RAJ!")

# no catch statement here, only in JAVA