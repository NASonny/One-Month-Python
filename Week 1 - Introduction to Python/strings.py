# Strings are text surrounded by quotes
# Both single ('') or double ("") or triple  (""") quotes are used 
# Examples : "dinosaurs", '8461185' , "I'm Lovin' it!"

wayne_quote = "If you change the way you look at things, the things you look at change."

print(wayne_quote)

#Use of triple quotes 

wayne_quote = """If you change the way 
you look at things, 
the things you look at change."""

print(wayne_quote)

#you can use single quotes in the double quotes

roosevelt_quotes = "Believe you can and you're halfway there."

print(roosevelt_quotes)


#If you want to use double quotes for some citations you can use \ to avoid the first double quotes

hamilton_quote = "Well, the word got around, they said, \"This kid's insane, man\""

print(hamilton_quote)



name = "Mattan Griffel"
orphan_fee = 200
teddy_bear_fee = 121.8

total = orphan_fee + teddy_bear_fee


#We can use f before double quotes to use bracket to get the variables in the quotes so there is no need to leave the quotes to use a variable 
print(f"{name} the total will be {total:.2f}")
#:.2f are for the matter of the float, so we are going to get just two numbers after the dot.

