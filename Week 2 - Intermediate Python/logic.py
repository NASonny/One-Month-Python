
#! If you currently try to compile the file, that will not work you need to comment all the comparison with an error

answer = input("Do you want to hear a joke?")

affirmative_responses = ["Yes", "yes", "y", "Y"]
negative_responses = ["No", "no", "n", "N"]

#We are checking if the input is equal to Yes or yes
if answer in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
#We are checking if the answer is no 
elif answer in negative_responses:
    print("Fine.")
#Here is if the answer is not No and not Yes so we print Idu.  
else:
    print("I don't understand.")

######## Version with less code and no list but still works but not optimized ########


if "y" in answer.lower():
    print("I'm against picketing, but I don't know how to show it.")
elif "n" in answer.lower():
    print("Fine.")
else:
    print("I don't understand.")


########  ######## ######## ######## ######## ######## ######## ######## ######## ########
    
############### Version with .lower or .upper ###############


affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")


############### ############### ############### ############### 


if True:
    print("") # Anything will run here if you input the right answer we want
if False:
    print("") # Never run


####### LOGIC ####### 

not True == False
    
not False == True


#Code "=="

1 == 1 = True 
1 == 0 = False
0 == 1 = False
0 == 0 = True


#Code "and"

True and True = True
True and False = False
False and True = False
False and False = False

#Code "or"


True or True = True
True or False = True
False or True = True
False or False = False


#Code "in"

people[..., ..., ...]
if .... in people:
    print("")

############### ############### 