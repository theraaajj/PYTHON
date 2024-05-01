# TUPLES : immutable

tup = (87, 88, 89, 55, 64, 78)
print(tup[0])

# tup[2] = 43         # not item assignment

name = ()
# valid. can be a empty tuple

bro = (1,)          # single elem tuple. comma necessary
siso = (1)          # will be treated as an integer

#slicing possible (same as always)
print(tup[1:4])


tup = (2, 1, 3, 1)

print(tup.index(1))
print(tup.count(1))

# immutable: no such attributes
tup.sort()
tup.reverse()
tup.append()
tup.remove()
tup.pop()