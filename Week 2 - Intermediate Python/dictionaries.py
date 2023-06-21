# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

# How to create a Dictionaries
states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

#with print(states['NY']) we are going in to check the values of the key 'NY' so in this case this is New York.
print(states['NY'])

print(type(states))

print(states.get('FL', 'Not found'))
print(states.get('NY', 'Not found'))

print(states.keys())
print(states.values())

states['FL'] = 'Florida'
print(states)

# The use of dictionaries is to be more precise than a list because we don't know what is the values of what in a list.
# user = ['Mattan', 70, 10.5, 'Brown', 'Brown']
user = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

print(user['name'])

# Dictionaries and lists can be inside of each other.

animal_sounds = {
    "cat": ["Meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": [],
}

mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}
sarah = {'name': 'sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = [mattan, chris, sarah]
print(people)

for person in people:
    print(person['name'],person['height'])

print(person.get('height'))
