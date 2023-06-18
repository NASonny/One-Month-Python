name = input("What's your name ? ")

#age = input("How old are you ? ") Will return a string so if you want to use it in interger you need to do what is below so add int before the input()
age = int(input("How old are you ? "))
#age = float(input("How old are you ? "))
age_in_dog_years = age * 7

print(f"Your name is {name}, you'r {age_in_dog_years} in dog years")