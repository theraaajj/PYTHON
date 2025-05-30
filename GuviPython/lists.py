l=[1,2,3,4,5,6,7]
l.remove(l[2])
print(l)
#[1, 2, 4, 5, 6, 7]

l.remove(2)
print(l)
#[1, 4, 5, 6, 7]

#remove() simply removes a spcified element directly or indirecty through an index provided


l.append(8)
print(l)
#[1, 4, 5, 6, 7, 8]

l.append(2)
print(l)
#[1, 4, 5, 6, 7, 8, 2]

#append() adds an element to the last of the list


#how to copy an existing list into a new list?
mylist1 = ["Raj", "Anushka", "Khushi"]
newlist = mylist1.copy()
print(newlist)
