def greet(name):
    return f"Hey {name}!"

def concatenate(word_one, word_two):
    return word_one + word_two

def age_in_dog_years(age):
    result = age * 7
    return result

# Be sure to give the right number of arguments to not give too much or less than necessary 
print(greet("Epitech"))
print(greet("Chris"))

print(concatenate("Hello", " World!"))
# If you precise you can switch the word 
print(concatenate(word_two='Mattan', word_one="Griffel"))

# If you don't return correctly, Python just are saying going None to the result when you print it
print(age_in_dog_years(20))

"""
def age_in_dog_years(age):
    result = age * 7
    #return result
"""

name = "Sonny"
def print_different_name():
    name = "Chris"
    print(name)

print(name)
print_different_name()
print(name)

####### My Challenges functions #######

def uppercase_and_reverse(word):
    name = word.upper()
    reverse_word = name[::-1]
    return(reverse_word)

print(uppercase_and_reverse("hello")) #Result we want OLLEH  

##########################################


############## Shortest Solution ##############

def uppercase_and_reverse(text):
    return text.upper()[::-1]

print(uppercase_and_reverse("banana"))

##############################################