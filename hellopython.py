import random
import sys
import os
'''
print("Hello World")

name = '"Ankush'
lname = 'Saini Age - 27'

newstring = name + lname
print(newstring)

print("%s %s %s" % ('My name is',name, lname))

print("I don't like", end=" ")
print("newlines")
'''
day = ['sun', 'mon', 'tue', 'wed']
month = ['jan', 'feb', 'mar', 'apr']
'''
print(day[1:4])
day_month = [day, month]

print(day_month)
print(day_month[0][2])

month.append('may')
print(month)

day.insert(4, 'thu')
print(day)

day.remove('thu')
print(day)

day.sort()
print(day)

day.reverse()
print(day)

new = day + month

print(new)
print(min(new))

oddn_tuple = (1,3,5,7,9)

print(oddn_tuple)

newl = list(oddn_tuple)
print(newl)
newt = tuple(newl)
print(newt)

print(max(newt)

l_conve = {'Onion':'Pyaaz',
         'Potato':'Aloo'}

print(l_conve['Potato'])

del l_conve['Onion']

print(l_conve)
print(l_conve.keys())
print(l_conve.values())

a = 99
b = 8
if a > b :
    print('a is bada')
elif a == b:
    print('Ma Man')
else:
    print('b is bada')

c = a / b
print(c)

if ((a>5)and(b<7)):
    print('case I')
elif (c<2):
    print('case II')
elif not(a<b):
    print('case III')
else:
    print('case IV')


for x in range(0,3):
    print(x)
for y in month:
    print(y,end=' ')

numlist = [[1,2,3],[10,20,30],[100,200,300]]

print(numlist)

for x in range(0,3):
    for y in range(0,3):
        print(numlist[x][y], end=" ")

print('\n',numlist[2][2])


randomnm = random.randrange(0,100)

while (randomnm != 9):
    print(randomnm, end=' ')
    randomnm = random.randrange(0, 10)

i = 0

while (i <= 30):
    if (i%3 == 0):
        print(i,end=' ')
    elif (i==26):
        break
    else:
        i += 1
        continue
    i += 1

    # Understanding break
number = 0

for number in range(10):
    number = number + 1
    if number == 5:
        break  # break here
    print('Number is ' + str(number))

print('Out of loop')

# Understanding continue
number = 0

for number in range(10):
    number = number + 1
    if number == 5:
        continue
    print('Number is ' + str(number))

print('Out of loop')

# Understanding pass
number = 0

for number in range(10):
    number = number + 1
    if number == 5:
        pass
    print('Number is ' + str(number))

print('Out of loop')

# An iterator for a while loop is defined before the loop
i = 0;
while (i <= 20):
    if (i % 2 == 0):
        print(i)
    elif (i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue

    i += 1


# FUNCTIONS -------------
# Functions allow you to reuse and write readable code
# Type def (define), function name and parameters it receives
# return is used to return something to the caller of the function
def addNumbers(fNum, sNum):
    sumNum = fNum + sNum
    return sumNum


print(addNumbers(1, 4))

# Can't get the value of rNum because it was created in a function
# It is said to be out of scope
# print(sumNum)

# If you define a variable outside of the function it works every place
newNum = 0;


def subNumbers(fNum, sNum):
    newNum = fNum - sNum
    return newNum


print(subNumbers(1, 4))

# USER INPUT -------------
print('What is your name?')

# Stores everything typed up until ENTER
name = sys.stdin.readline()

print('Hello', name)

# STRINGS -------------
# A string is a series of characters surrounded by ' or "
long_string = "i ain't a tweener"

# Retrieve the first 5 characters
print(long_string[0:5])

# Get the last 5 characters
print(long_string[-5:])

# Everything up to the last 5 characters
print(long_string[:-5])

# Everything after the last 5 characters
print(long_string[-5:])

# Concatenate part of a string to another
print(long_string[:4] + "bcde")

# String formatting
print("%c sky full of %s with count %d precisely %.3f" % ('A', 'stars', 100, 100.99))

# Capitalizes the first letter
print(long_string.capitalize())

# Returns the index of the start of the string
# case sensitive
print(long_string.find("ain"))

# Returns true if all characters are letters ' isn't a letter
print(long_string.isalpha())

# Returns true if all characters are alphanumeric
print(long_string.isalnum())

# Returns the string length
print(len(long_string))

# Replace the first word with the second (Add a number to replace more)
print(long_string.replace('tweener', 'nigger'))

# Remove white space from front and end
print(long_string.strip())

# Split a string into a list based on the delimiter you provide
quote_list = long_string.split(' ')
print(quote_list)
'''
# FILE I/O -------------

# Overwrite or create a file for writing
test_file = open("test.txt", 'wb+')

# Get the file mode used
print(test_file.mode)

# Get the files name
print(test_file.name)

# Write text to a file with a newline
test_file.write(bytes("Tweener is back\n", 'UTF-8'))

# Opens a file for reading and writing
test_file = open("test.txt", "r+")

# Read text from the file
print(test_file.read())

# Close the file
test_file.close()

# Delete the file
os.remove("test.txt")
'''

# CLASSES AND OBJECTS -------------
# The concept of OOP allows us to model real world things using code
# Every object has attributes (color, height, weight) which are object variables
# Every object has abilities (walk, talk, eat) which are object functions

class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __name = None
    __height = None
    __weight = None
    __sound = None

    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, height):
        self.__height = height

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)

    def get_weight(self):
        return str(self.__weight)

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight,
                                                                      self.__sound)


# How to create a Animal object
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())


# You can't access this value directly because it is private
# print(cat.__name)

# INHERITANCE -------------
# You can inherit all of the variables and methods from another class

class Dog(Animal):
    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None

        # How to call the super class constructor
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    # We can overwrite functions in the super class
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(),
                                                                                       self.get_height(),
                                                                                       self.get_weight(),
                                                                                       self.get_sound(), self.__owner)

    # You don't have to require attributes to be sent
    # This allows for method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)


spot = Dog("Spot", 53, 27, "Ruff", "Derek")

print(spot.toString())


# Polymorphism allows use to refer to objects as their super class
# and the correct functions are called automatically

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
'''