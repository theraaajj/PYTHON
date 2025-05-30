s1={}
print(type(s1))                     #<class 'dict'>

s2={1,2,3,4}
print(type(s2))

#declaring a dictionary data structure
d1={'a':1, 'name':"Raj"}                          #this mean 'a' is the key and 1 is it's value
print(d1)
print(type(d1))

#indexing in a dictionary. there's no index value, instead there's the key.
print(d1['a'])
print(d1["name"])

#key cannot contain any special character in it's naming convention,
#until and unless it's in form of strings...


d2 = {'name':'raj', 'name':'anushka'}
print(d2)
#unique key hona chahie warna overwrite kardega old value ko,new value se.

#different operations on dictionary
d3 = {'name':"Raj", 'Email':"raj@gmail.com", 'subject':['OS', 'MP', 'Python']}
print(d3)
print(d3['subject'])
print('Python' in d3['subject'])
print(d3['subject'][2])

#adding a new key
d3['hobbies'] = ['cycling','painting']
print(d3)

#same tarike se update bhi kar skte hain
d3['name']='Anushka'
print(d3)
#{'name': 'Anushka', 'Email': 'raj@gmail.com', 'subject': ['OS', 'MP', 'Python'], 'hobbies': ['cycling', 'painting']}


#how to delete any particular key from dict?
del d3['Email']
print(d3)
#capslock ka dhyan dena

#how to display all the keys and all the values?
print(d3.keys())
print(d3.values())

#how to store the keys or values in a list?
x= list(d3.keys())
y= list(d3.values())
print(x, y)

#how to display all the keys and all the values together?
print (d3.items())

#isko bhi same tarike se list me store kar sakte hain.

#lastly deletion of a dictionary
d3.clear()
print(d3)

"""done boii. dictionary is intensively used in json packages, databases,
file transfer over the internet or between 2 applications. moreover mondoDB
me bhi somewhat iska concept help karega."""