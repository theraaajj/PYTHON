f = open("01_helloWorld.py", "r")
print(f.read())
f.close()
# close is necessary here to clear the cache and unecessary buffer space

# +++++++++++++++++++++++ #

with open("01_helloWorld.py", "r") as f1 : 
    print(f1.read())                            # no need to close here, automatically done

# check other opening modes and functions of file handling

# +++++++++++++++++++++++ #

