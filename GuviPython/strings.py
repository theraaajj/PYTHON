x = "Hello world"

#indexing
print(x[2])
#slicing
print(x[0:3])
print(x[0:])
print(x[0::2])
print(x[-5:-1])

#multiline strings
a = """My name
    is Raj Aryan,
    and I live in
    Greater Noida."""
b = '''Tell me
       something 
       about yourself'''

#concatenation
print(x+a)
print(x+" "+a)

c = a+b

#length
print(len(c))
#membership operator
print ("Raj" in c)

