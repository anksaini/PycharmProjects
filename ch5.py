# Demonstrates lists

# create a list with some items and display with a for loop
grocery = ["onion","tomato","carrot","banana"]
for i in grocery:
    print(i)

input("\nPress the enter key to continue.")

# get the length of a list
print("You have",len(grocery)," items with you")

input("\nPress the enter key to continue.")

# test for membership with in
if "onion" in grocery:
    print("you have the very basic veggie")

# display one item through an index
index = int(input("Enter the index: "))
print("You have ",grocery[index]," stored at index ",index)

# display a slice
s=int(input("Enter beginning index: "))
e=int(input("Enter ending index: "))
print(grocery[s:e])
input("\nPress the enter key to continue.")

# concatenate two lists
moregrocery = ["eggs","milk"]
grocery += moregrocery
print(grocery)
for i in grocery:
    print(i)

input("\nPress the enter key to continue.")

# assign by index
grocery[2] = "chicken"
print(grocery)

input("\nPress the enter key to continue.")

# assign by slice
grocery[0:2]=["cheesesteak"]
print(grocery)

input("\nPress the enter key to continue.")

# delete an element
del grocery[1]
print(grocery)

input("\nPress the enter key to continue.")

# delete a slice
del grocery[0:2]
print(grocery)
input("\n\nPress the enter key to exit.")

# p129
# High Scores
# Demonstrates list methods
scores = []
choice = None
print('''
0 - Exit
1 - Show
2 - Add
3 - Remove
4 - Sort
''')
while choice != "0":
    choice = input("Enter a choice: ")
    if choice == "0":
        continue
    elif choice == "1":
        for i in scores:
            print(i)
    elif choice == "2":
        score = int(input("Enter the score: "))
        scores.append(score)
        print(scores)
    elif choice == "3":
        score = int(input("Enter the score: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Score ain't there")
            continue
        print(scores)
    elif choice == "4":
        scores.sort(reverse=True)
        print(scores)
    else:
        print("You ain't entering valid choices")

print("Go-fuck-yourself")

