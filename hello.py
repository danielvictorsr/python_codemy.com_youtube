import os #interation with operational system
os.system('clear') #clear the Screen

'''
All in this bloack will be
commentary.
Open and close with 3 simple quotes
'''

full_name = "John Elder"
fuly = ame = "ten"

#Convention in Python _ >>> full_name

# Print Hello World To The Screen
print("Hello World!", full_name, fuly, ame)


'''
Summary: 
Lists
Turples
Dictionary
'''

#Lists
names = ["John", full_name, ame]
print(names)

#Tuples - Lists don't modify |More faster - example google search 1 miliseconds more faster
names_tuples = ("1", "2", "3")
print(names_tuples)

#Dictionaries n information the same thing | two parts: 1 - key 2 - value
fav_pizza = {
	"John": "Pepperoni", #key:value
	"Bob": "Mushroom",
	"Mary": "Cheese"
}

#another way Dictionaries declarations | not good for read
fav_pizza2 = {"John": "Pepperoni","Bob": "Mushroom","Mary": "Cheese"}

print(fav_pizza["John"])