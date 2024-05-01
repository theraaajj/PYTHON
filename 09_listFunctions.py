list = [2, 1, 3]


# some of the functions are:
# index(elem)
# count(elem)
# remove(elem)
# insert(index, elem)
# pop(index)
# reverse()
# sort()
# append


# append('') : adds element to the last
list.append(4)
print(list)
# list.append("raj")       # can append a STRING but it won't SORT() then
# print(list)

# sort() : ascending by default
list.sort()               # returns a None value, therefore can't be used with print()
print(list)

# descending
list.sort(reverse=True)
print(list)

# reverses the list
list.reverse()
print(list)

# inserts at a given element : list.insert(index , elem)
list.insert(2, "Raj")
print(list)

# remove(elem) : removes the first occurence of gvn element
myList = [1, 2, 3, 4, 5 , 6, 7, 1, 2, 3]
myList.remove(3)
print(myList)             # [1, 2, 4, 5, 6, 7, 1, 2, 3]

# pop(index) : removes element from the given index
myList.pop(8)
print(myList)              # [1, 2, 4, 5, 6, 7, 1, 2]

hola = [1, 2, 3 , 1]
print(hola.index(3))
print(hola.count(1))