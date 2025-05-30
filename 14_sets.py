# SETS : collection of unordered items and is mutable
# each element must be unique and immutable
# gives a random arrangement of it's element , i.e. no fixed chronology 

nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}
# repeated elements stored only once, so it resolved to {1, 2}

null_set = set()       # empty set syntax

collection = {1, 2, 3, 4, 4, 1, "Raj", "Raj"}
print(collection)
print(type(collection))


mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(2)                # won't affect anything
mySet.add((1, 2, 3, 4))     # tuples can be easily added
# mySet.add([1, 2, 3, 4])     # can't add list or dictionary, as it's elem can be changed
print(mySet)

# anything that is immutable can be added to a SET 

# ........................................................

# SET Methods

# set.add(el)        adds the given element
# set.remove(el)     remove the given element
# set.clear()        empties the set
# set.pop()          removes a random value

print(len(mySet))
mySet.remove(2)
print(mySet)
mySet.pop()
print(mySet)


# set.union(set2)              combines both the set values and returns new
# set.intersection(set2)       combines common values in the 2 sets and returns new
# won't affect the actual sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))


# ...........................................
# ...........................................
givenSet = {"Python", "JAVA","C++", "Python", "JS", "JAVA", "Python", "JAVA", "C++", "C"}
print(len(givenSet))

# Store 9, 9.0 in a set as seperate value
values= {
    ("int", 9),
    ("float", 9.0)
}
print(values)