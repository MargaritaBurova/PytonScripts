import random

person = open("character.txt", "r")
persons = person.read()
print(persons)
person.close()

file = open("output.txt", "a+")