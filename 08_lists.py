# LISTS: mutable
#  sort of equivalent to array datatype
#  can store elements of different data types

marks = [94.5, 57.9, 42.0, 56.3, 76.8]     # square brackets, seperated by commas.
print(marks)
print(type(marks))                         # <class 'list'>


# quite common to strings.
# length
print(len(marks))
# indexing
print(marks[0])
# slicing

print(marks[0:2])              # [94.5, 57.9]
print(marks[:2])               # [94.5, 57.9]
print(marks[:])                # [94.5, 57.9, 42.0, 56.3, 76.8]
print(marks[2:])               # [42.0, 56.3, 76.8]
print(marks[-4:-2])            # [57.9, 42.0]
print(marks[-2:-4])            # []    but won't show any errors!

# slightly different from arrays.
# arrays store elements of same types generally
# but lists store diff types together. eg:
intro = ["Raj", 21, 90.2, "PNBE"]
print(intro)
print(type(intro[0]))
print(intro[0][2])


# strings are immutable, i.e. can be accessed through indexing (no item assignment)
# but can't be changed. lists can be changed using indexing.
intro[1] = 21.5
print(intro)