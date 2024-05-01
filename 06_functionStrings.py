str = "i am raj aryan"

# .endswith("")
print(str.endswith("yan"))
print(str.endswith("yan."))

# .capitalize() : capitalizes the first letter of the sentence.
print(str.capitalize())

# .title() : capitalizes the first alphabet of each word in a sentence.
print(str.title())

# .replace("", "")
print(str.replace(" ", "_"))
naam = str.replace("raj aryan", "boogie man")
# print(str.replace("raj aryan", "boogie man"))
print(naam)



# .find()
print(str.find("am"))        # gives index of the first letter of given word, in it's first occurence
print(str.find("r")) 

# .count()
print(str.count("a"))
print(str.count(" "))