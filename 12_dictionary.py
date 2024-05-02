# Dictionaries: key:value pairs , mutable, unique keys

dict = {
    "name" : "Raj",
    "cgpa" : 7.5,
    "marks": [23, 45, 73, 29],
    12.99  : 1.99,
    46     : "HelloRaj" 
}
print(dict)        # {'name': 'Raj', 'cgpa': 7.5, 'marks': [23, 45, 73, 29]}

print(dict["name"])
print(dict[12.99])
# print(dict["surname"])           # error

# can change the value of a key
dict[46] = 99.99           # overwrite
print(dict)


# creating a null dictionary
abc = {}
# adding a value
abc["name"] = "RAJ"
print(abc)


# Nested Dictionaries.
# key ki kisi value ko khud me dictionary bana sakte hain

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
print(dict2)        # {'name': 'Raj', 'cgpa': 7.5, 'marks': [23, 45, 73, 29], 'subject': {'maths': 96, 'eng': 95, 'hindi': 95}}  
print(dict2["subject"]["maths"])           # 96