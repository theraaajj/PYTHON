x = "Raj Aryan"
print(x.upper())
print(x.lower())
print(x.swapcase())

y = "   Anushka Sharma    "
print(y.strip())
print(y.split(" "))
print(y.replace("u","o"))
print(y.split("a"))
print(y.replace(" ","a"))

y = y.casefold()
print(y.capitalize()) #since phle letter upper case me jata hai, aur yaha blank space hai
print((x.lower()).capitalize()) #pehle x ko lower case kiya aur tab capitalize lagaye.

z = 'Mohit Ranjan'
f="""print(y)
print(y.count("a"))
print(y.find("a"))
print(y.find("h"))
print(y.find("k"))"""

print (f.replace("y","z"))

print(z)
print(z.count("a"))
print(z.find("a"))
print(z.find("h"))
print(z.find("k"))
print(z.find("R"))

b1= """My name
    is Raj Aryan,
    and I live in
    Greater Noida."""
g=b1.just(b1)
print(g)


#Many of the string functions aren't working and i don't know why!
#Check for them in the copy.