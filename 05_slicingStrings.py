# Slicing: Accessing parts of a string.

# str[starting_index:ending_index] == ending index is not included.

str = "RAJ ARYAN"
print(str[1:3])
print(str[:4])   # equal to [0:4]
print(str[0:])   # equal to [0:len(str)]
print(str[:])    # equal to [0:len(str)]

naam = "Machine Learning"
print(naam[-5:-1])   # includes -5, but excludes -1
print(naam[:-1])     # equal to [start:-1]
print(naam[-8:])     # equal to [-8:len(naam)]
print(naam[:])       # prints the whole word