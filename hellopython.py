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
'''
# Understanding pass
number = 0

for number in range(10):
    number = number + 1
    if number == 5:
        pass
    print('Number is ' + str(number))

print('Out of loop')