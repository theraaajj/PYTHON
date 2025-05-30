num = [1,2,3,4,5,67,89,100]
for i in num:
    if i%2==0:
        print(i)   #beta identation bhut jruri hai, warna kahani khatam.. java ya c++ nhi h yeh.

name = "RAJ ARYAN"
for i in name:
    print (i)


#Question. Remove all the "a" from the sentence.
a = "raj aryan is a bastar boy of the age 20 who always play abracadabra"
for i in a:
    if i=="a":
        continue
    print (i)


#range() function
for i in range(100):
    print(i)

for i in range(40,100):
    print (i)

'''
i= 1
for i<6:      #wrng for i in range(6) ye shi hoga
   if i == 3:
      break
   i += 1
'''



#question for-loops
#list me se sara data type ka apna apna list bana ke store kro
mylist = [1,2,"raj", 4.23, "anushka", 5,6]
lint = []
lstr = []
lfloat = []
for a in mylist:
    if type(a) == int:
        lint.append(a)
    elif type(a) == float:
        lfloat.append(a)
    elif type(a) == str:
        lstr.append(a)
print(lint)
print(lfloat)
print(lstr)


#question for-loops and dictionary
#dictionary ke saare key value pairs ko print kro alag alag
d = {"name":["Raj","Anushka"],"age":[20,21],"state":"bihar","college":("KCC", "SRM")}
for i in d.items():      #items function isme lagega in scuh a case
    print(i)             #yaha nhi lagega

#jo bhi list ke form me value hai dict me, wo print kro
d = {"name":["Raj","Anushka"],"age":[20,21],"state":"bihar","college":("KCC", "SRM")}
for i in d.values():
    if type(i)==list:
        print (i)

#name me raj hai kya? check kro
for i in d.values():
    if type(i)==list:
        if "raj" in i==true:
            print("YES")
            break
    else:
        continue