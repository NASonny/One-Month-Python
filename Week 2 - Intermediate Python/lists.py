#Exemple of list in Python
the_count = [1, 2, 3, 4 , 5 , 6]
stocks = ["AAPL", "GOOG", "TSLA",]
random_things = ["Puppies", 55, 0, "Hello World", 1*2, 1/3]

# this for-loop goes through a list
for number in the_count:
    print("this is a count", number)

# same as above
for stock in stocks:
    print("Stock ticker:", stock)

#we can go through mixel lists too
#I called it i (short for item) since I don't know what's in it
for i in random_things:
    print("Here's a random thing:", i)
    
# we can also build lists, first let's start with an empty one
people = []

# We can add people like this from an empty list
people.append("Mattan")
people.append("Luke")
people.append("Ash")

print(people)

# We can also remove people from the list like this
people.remove("Luke")
print(people)

for person in people:
    print("Person is:", person)

# Challenge: Print out the square of the numbers 1 to 10

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in number:
    print("The square of",i,"is :", i**2)
    
#Shortest way 
for i in range(1, 11):
    print("The square of",i,"is :", i**2)


# here's how you acces elements of a list

animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

print("There are this many things:", len(random_things))
print("things is a:", type(first_animal))

another_list = random_things[-1]
print(another_list)
print(type(another_list))
