# take input of 3 movies and store them in a list
movies = []
mov1 = input("Enter a movie: ")
mov2 = input("Enter another movie: ")
mov3 = input("Enter another: ")
movies.append(input("Enter the fav movie"))
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


# important!
# check if a list is palindrome
list1 = [1, 2, 3, 2, 1]
copyofthislist = list1.copy()
list1.reverse()

if(copyofthislist == list1):
    print("yes")
else:
    print("no")



wow = ["A", "B", "C", "A", "D", "A", "B" ]
wow.sort()
print(wow)