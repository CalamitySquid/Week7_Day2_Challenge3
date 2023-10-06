# NAMES: GERARDO PINEDA, SEBASTIAN WONG, JESUS RUIZ, ISAAC MUNGUIA

########## SET-UP ##########
# Asks for short text input:
phrase = input("Provide a short text: ")
# The following 3 lines ask for the random letter:
random_letters1 = input("Type random letter here: ")
random_letters2 = input("Type random letter here: ")
random_letters3 = input("Type random letter here: ")
# Makes all letters and words inputed lowercase 
phrase_l = phrase.lower()
random_letters1_l = random_letters1.lower()
random_letters2_l = random_letters2.lower()
random_letters3_l = random_letters3.lower()

# # # 1 # # #How many times each letter appears:
num_list = [random_letters1_l, random_letters2_l, random_letters3_l]
# How many times letter 1 shows up (It counts how many times the letter appeared in the input):
num_of_letters1 = phrase_l.count(random_letters1_l)
print(str(num_of_letters1))
# How many times letter 1 shows up (It counts how many times the letter appeared in the input):
num_of_letters2 = phrase_l.count(random_letters2_l)
print(str(num_of_letters2))
# How many times letter 1 shows up (It counts how many times the letter appeared in the input):
num_of_letters3 = phrase_l.count(random_letters3_l)
print(str(num_of_letters3))

# # # 2 # # # Counting the amount of words in the phrase:
# Splits every word or clump of characters into an item in a list
cutting = phrase_l.split(" ")
# len() counts up each item in the list
num_of_words = len(cutting) 
print("Number of words:", num_of_words)

# # # 3 # # # Print the first and last letter in the phrase:
# First letter (takes the first index of 0):
print(phrase_l[0])
# Second letter (takes the last index with -1):
print(phrase_l[-1])

# # # 4 # # # Inverting the order of the words: 
# [::-1] Inverts the order of the words in the phrase
print(cutting[::-1])

# # # 5 # # # Looks for the word "python" in the inputed phrase
# Determines wether or not python is in the phrase inputed by the user
python_found = "python" in phrase_l
# If python is found in the inputed phrase then it will print out "python found: " and then if it's true or false
print("Python found:", python_found)
