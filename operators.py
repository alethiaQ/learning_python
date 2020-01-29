# basic addition, subtraction, multiplication
number = 1 + 2 * 3 / 4.0
print(number)

# modulo is used to deduce a remainer
remainder = 11 % 3
print(remainder)

# power symbol is made with two ** 
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# strings can be concatenated with operators
boopgoopdoop = "boop" + " " + "goop" + " " + "doop"
print(boopgoopdoop)

# you can multiply strings and lists with the operator and an interger to get a number of repeated strings
thisIsCoolTenTimes = "this is cool!" * 10
print(thisIsCoolTenTimes)

# lists can be joined simply by an additon operator
blue_food = ["blueberries"]
green_foods = ["grape", "apple"]
all_foods = blue_food + green_foods
print(all_foods)

# string literals are also concatenated automatically when directly next to each other
print('hey' 'you' 'guys')  # = heyyouguys


# slicing-- While indexing is used to obtain individual characters, slicing allows you to obtain substring:

word = "NutterButter"
new = word[0:2]
 # characters from position 0 (included) to 2 (excluded)
print(new)