"""Basically comprehension is an advance way of writing a block of code generally
having a loop with conditionals inside it, and turn it into a one-liner.
Dictionary comprehension, Set comprehension, aur Generator comprehension bhi hoti hain"""


#LIST COMPREHENSION

hisfruits = ["apple","mango","banana","orange","kiwi"]
herfruits = ["dragonfruit","apple","pomegrenate","orange"]
newlist = [x if x != "banana" else "orange" for x in hisfruits]
print(newlist)
#output as expected : ['apple', 'mango', 'orange', 'orange', 'kiwi']

newlist1 = [x.title() for x in herfruits]
print(newlist1)
#['Apple', 'Mango', 'Banana', 'Orange', 'Kiwi']

#ek list chahie 100 tak ki, with only nmbrs divisible by 3
newlist3 = [x for x in range(100) if x%3==0]
print(newlist3)#successful execution


#DICTIONARY COMPREHENSION

#agar ek dictionary print krna ho like: dict = {0:"item0",1:"item1",......upto 100}
newdict = {i:f"item{i}" for i in range(101)}
print(newdict)

newdict1 = {i:f"item{i}" for i in range(1,101)}
print(newdict1)

#same conditions but only evem numbers:
newdict2 = {i:f"item {i}" for i in range(101) if i%2==0} #f".... is an another topic called fstrings
print(newdict2)

#agar key value pair ko exchange karna ho tab
newdict3 = {value:key for key,value in newdict2.items()}
print(newdict2,"\n",newdict3)

