import random

# p102
'''
word = input("Enter a string")
v = "aeiou"
nword = ""

for i in word:
    if i.lower() not in v:
        nword += i
        print("Word is ",nword)

# p116,120/3

words = ("python","java","C++","angularjs","reactjs","html")

# print(len(words))
word = random.choice(words)
# print(len(word))
correct = word
jumbled = ""

while word:
    i = random.randrange(len(word))
    jumbled += word[i]
    word = word[:i] + word[i+1:]

print(jumbled)

guess = input("Guess language :")

while guess != correct:
    resp = input("Wrong! Need Hint?Yes/No ")
    if resp.lower() == "yes":
        print("Hint : ",correct[0],correct[1])
    else:
        print("Then Try Again")
    guess = input("Enter word :")

if guess == correct:

    print("Correct")

# p120/1
i=0
s = int(input("Starting number:"))
e = int(input("Ending number:"))
c = int(input("Common Difference:"))

for i in range(s,e+1,c):
    print(i, end=" ")
    i += 1

# p120/2
message = input("Enter the message: ")

for i in range(len(message),0,-1):
    print(message[i-1], end="")
'''
# p120/4
print("Guess the fruit!")
words = ("apple","mango","guava","grapes","banana","cherry","orange","papaya","cranberry")

word = random.choice(words)

print("Number of letters : ",len(word))

for i in range(len(word)):
    guess = input("Guess a letter : ")
    if guess not in word:
        print("No, Attempt(s) left: ", (len(word)-(i + 1)))
        continue
    else:
        print("Yes, ",guess,"is in the word")

final = input("Enter the fruit")

if final.lower() == word:
    print("Cool")
else:
    print("You are just another piece of shit!")
