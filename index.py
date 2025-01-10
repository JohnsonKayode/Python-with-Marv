#Numbers

number1 = 50    #integer(Whole numbers)
number2 = 80.9  #float (Decimal numbers)

#string

name1 = 'This is a string'  #string
name2 = "This is also a string"   #string

name3 = '''This is a string
that cuts accross lines
or lets say multiple lines of code. But still is a string'''

firstletter = name1[0] #this prints the first letter in name1 variable which is 'T', and we can do the same for the rest, by indexing their numbers
print(firstletter)
#the syntax for string slicing is string[start:end:steps]
name4 = name1[0:5:2] # so this code takes the first letter at index[0], skips 2 letters and picks the next letter. 

#string methods
# .upper() - gives us our strings in all upper case
# .lower() - gives us our strings in all lower case
# .strip() - removes leading an dtrailing whitespaces
# .replace() - This replaces a specified phrase with another specified phrase
# .split() - Split strings into a list, where each word is a list item. 

name5 = '      Johnson Kayode'

name_upper = name5.upper()
name_lower = name5.lower().strip()
name_strip = name5.strip()
name_split = name5.split()
name_replace = name5.replace('Johnson','Emmanuel')


print(name_split[1])

#concatenaing strings
message = f'{name5} says Good morning to you {name_replace}'
print(message)

#Booleansv


#Data structures

# Lists is an ordered collection of items, the values are changeable 
my_list = [1,2,3,4,5]
# For lists you use the Square barackets 

# Tuples are collection of items- You cannot change the values of tuples
names = ('Johnson', 'Kayode', 'Emmanuel')
# For lists you use the regular curve brackets

# Dictionary
user = {'name' : "johnson Kayode", 'School': 'Altschool Africa', 'Year of Admission' : 2024}
# This is a user with key value pairs. Name, school and year of admission. The keys must be unique and are used to retrieve the corresponding values. They are separated by commas

print(user['Year of Admission'])

# Set is like a list but it takes out duplicates -
my_list = {1,2,4,1,6,3,4,5,5,}
#for sets, you use a curly braces

print(my_list)

#boolean operators 

#Using the true of false statement
is_raining = True
not_raining = False

if (is_raining == True):
    print(f'It is {is_raining}, it is raining and you do not need to go out') 
else:
    print(f'it is {not_raining}, you can go outside and have fun')

#Comparison booleans
number3 = 10 
number4 = 20

print(number3 == number4)
print(number3 < number4)

#Logical operators
statement1 = True
statement2 = False

print(statement1)

#Conversion function - int(), str(), float(), bool()

x: int = 20 #like saying x = 20. But with the 'int' keyword, it is specifying what type of value to be passed to X
y: str = str(x) #what this line is doing, is specifying that variable Y should only accept a string value, and the str() function is converting the integer X to a string and assigning it to Y. so X is an integer 20, but Y is a string '20'.

print(type(x))

#If condition statements

#a control flow in python describes the order in which the code runs

#if statement in python

guess = 0

if guess < 20 or guess > 20:
    print(f'This is wrong, try again. The correct number is {guess}')
else: #always add the colon in front 
    print(f'We won, the number is {guess}')

#for loop in python
#This is used for iterating a sequence (lists, tuples, dicionaries and others)

for i in name2:
    if i == 's':
        continue # Continur could also be considered as a SKIP in a for loop
#    elif i == 'o':    
#       break # tells the loop to stop running 

    print(i)

#while loop

#The while loop checks a condition before running and if the condition is false, the code will not run

count = 0
max = 10

while count < 100:
    print(f'count {count} is less than {max}')
    count += 1
    if count == max:
        text = f'Now count {count} is now equal to {max}'
        print(text)
        break

# using the for loop to repeat the same thing done using the while loop 
for count in range(max + 1):
    if count < max:
        print(f'count {count} is less than {max}')
        count += 1
    elif count == max:
        text = f'Now count {count} is now equal to {max}'
        print(text)
        break

#function 
#A function is a block of code that performs a specific task. could be reused multiple times as well within the same code. Some functions return a value or no value at all 

#they are designed using the def keyword followd by the name of the function. and maybe parenthesis if needed. Functions may take arguements or not. These arguements are used to pass a value that would be used within the function body/code. Pyhton has some already made functions that we can use or we can also create our own

#always add your colon

def firstFunction():
    return f'Hello World, This is my first function'

#output = firstFunction()
print(firstFunction())