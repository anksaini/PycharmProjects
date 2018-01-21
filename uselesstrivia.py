import random
import sys
import os

name = input("What's your name?")
age = int(input("How old are you?"))
weight = int(input("Okay, last question. How many pounds do you weight?"))

print("if poet ee cummings were to email you, he'd address you as ",name.lower(),".But if ee were mad, he'd call you ",name.upper())

print("If a small child were trying to get your attention your name would become: ", name*5)

print("You're over ",age*365*24*60*60,"seconds old")

print("Did you know that on the moon you would weigh only ",weight/6,"pounds?")
print("On the sun, you'd weigh ",weight*27.1,"<but, ah... not for long>")