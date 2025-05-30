fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(*green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#syntax error kyuki unpacking time do element me asterick nhi hoga bey gadhe!