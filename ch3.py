import random
import sys
import os

# p51
'''
die1 = random.randint(1,6)
die2 = random.randrange(6)+1

print("You rolled a ",die1," and a ",die2," for a total of ",die1+die2)


#p54
password = input("Enter password : ")

if password == "secret":
    print("Access granted")
    print("You important")
else:
    print("Access denied")
    print("You ain't important")
print("you always "
      "get this")


# p64
response = ""

while response != "cuz":
    response = input("Why?\n")

print("oh okay")

i = 0
while i<=10:
    print(i)
    i += 1
print(i)



count = 0

while True:
    count += 1
    if count > 10:
        break

print(count)


randnum = random.randint(1,100)
t = 3
print("You have ",t+1," tries")
picknum = int(input("Guess the number between 1 to 100\n"))
i = 0
while randnum != picknum and t !=0 :
    if picknum > randnum:
        t -= 1
        print(t+1," tries left",end=".")
        picknum = int(input("Smaller!\n"))
    else:
        t -= 1
        print(t+1, " tries left",end=".")
        picknum = int(input("Larger!\n"))
    i += 1
if picknum == randnum:
    print("Correct! You guessed it in ",i," tries")
else:
    print("Number was ",randnum,".You outta tries, Nigga")

# p85/1

randnum = random.randrange(1,6)
print(randnum)
if randnum == 1:
    print("Sex")
elif randnum == 2:
    print("Money")
elif randnum == 3:
    print("Job")
elif randnum == 4:
    print("Peace")
else:
    print("Gold")

# p85/2
head = 0
tail = 0

flip = random.randint(1,2)
i=0

while i !=100:
    if flip == 1:
        head += 1
    else:
        tail += 1
    flip = random.randint(1, 2)
    i += 1

print("Number of Heads : ",head)
print("Number of Tails: ",tail)
'''
# p85/4

picknum = int(input("Pick up a random number between 1 & 100\n"))
randnum = random.randint(1,100)
i=0

while picknum != randnum:
    print(randnum, end=" ")
    if picknum == randnum:
        break
    else:
        randnum = random.randint(1, 100)
    i += 1
print("\nComputer guessed it in",i,"tries")

