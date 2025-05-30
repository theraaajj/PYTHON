# DICTIONARY MTEHODS:
# dict.keys()             = returns all keys
# dict.values()           = returns all values
# dict.items()            = returns all (key, value) pairs as tuples
# dict.get("key")         = returns the key according to value
# dict.update(new Dict)   = inserts the specified items to the dictionary

dict2 = {
    "name" : "Raj",
    "cgpa" : 7.5,
    "marks": [23, 45, 73, 29],
    "subject" : {
        "maths":96 ,
        "eng":95,
        "hindi":95
    } 
}

print(dict2.keys())       # nested wali keys nhi aayengi
# dict_keys(['name', 'cgpa', 'marks', 'subject'])
print(dict2["subject"].keys())      # accessed the nested keys
# dict_keys(['maths', 'eng', 'hindi'])

### important
### type casting to a list & tuple
print(list(dict2.keys()))
print(tuple(dict2["subject"].keys()))

# number of key?
print(len(dict2))
print(len(list(dict2.keys())))
print(len(dict2["subject"]))

#same for values


print(dict2.items())         # returns each pair key;value in form of different tuples

print(dict2.get("name"))

# print(student["name2"])  :  ERROR
# print(dict2.get("name2"))  : no error  (None)

# update(newDict) : inserts items to our dictionary
newDict = {"City":"Delhi"}         # same key me new value daalne se overwrite hoga, kyuki same keys nhi hoskte, only unique
dict2.update(newDict)
print(dict2)

print(len(dict2))