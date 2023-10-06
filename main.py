# NAMES: GERARDO PINEDA, SEBASTIAN WONG, JESUS RUIZ, ISAAC MUNGUIA

########## SET-UP ##########
phrase = input("Provide a short text: ")
random_letters1 = input("Type random letter here: ")
random_letters2 = input("Type random letter here: ")
random_letters3 = input("Type random letter here: ")
phrase_l = phrase.lower()
random_letters1_l = random_letters1.lower()
random_letters2_l = random_letters2.lower()
random_letters3_l = random_letters3.lower()

# # # # # FINISHED CODE # # # # # # #
# # 1
num_list = [random_letters1_l, random_letters2_l, random_letters3_l]
num_of_letters1 = phrase_l.count(random_letters1_l)
print(str(num_of_letters1))
num_of_letters2 = phrase_l.count(random_letters2_l)
print(str(num_of_letters2))
num_of_letters3 = phrase_l.count(random_letters3_l)
print(str(num_of_letters3))

# # 2
cutting = phrase_l.split(" ")
num_of_words = len(cutting)
print("Number of words:", num_of_words)

# # 3
print(phrase_l[0])
print(phrase_l[-1])

# # 4
print(cutting[::-1])

# # 5 
python_found = "python" in phrase_l
print("Python found:", python_found)
