import random

person = open("character.txt", "r")
persons = person.read()
print(persons)
person.close()

status = ["live", "died"]
personLive = [f"{random.choice(status)}"]

print(personLive)

output = open("output.txt", "a+")
for line in personLive2:
    outputs.write(line)
    
outputs.close
