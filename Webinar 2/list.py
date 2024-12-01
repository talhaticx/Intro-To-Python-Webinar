#################################
#       ### Datatypes ###       #
#################################

strVar = "hello23"
intVar = 101
boolVar = True

listVar = ["hello", "hi", "uet", "iet"]

#################################
#         ### Lists ###         #
#################################

Fruits = ["apple", "banana", "orange", "mango", "kiwi"]

Evens = [2, 4, 6, 8, 10]

mixList = ["abc", 34, True, 40, "male"]

#################################
#         ### Index ###         #
#################################

# print(Fruits[0])  # Output: apple
# print(Fruits[2])  # Output: orange

# print(mixList[2]) # Output: True

# # Negative Indexing
# print(Fruits[-1]) # Output: kiwi

# Range of indexes
# print(Fruits[1:3])
# print()
# print(Fruits[:4])
# print()
# print(Fruits[2:])
# print()
# print(Fruits[-4:-1])

### in Keyword

# if "apple" in Fruits:
#     print("Apple is in the Fruits List")

#################################
#     ### Change Values ###     #
#################################

# print(Fruits)
# Fruits[3] = "grapes"
# print(Fruits)

# print(Fruits)
# Fruits[1:3] = ["blackcurrant", "watermelon"]
# print(Fruits)

#################################
#     ### Adding Values ###     #
#################################

# print(Fruits)
# Fruits.insert(2, "berries")
# print(Fruits)

# print(Fruits)
# Fruits.append("peach")
# print(Fruits)

# print(Fruits)
# Fruits.extend(["cherry", "pineapple", "papaya"])
# print(Fruits)

#################################
#    ### Removing Values ###    #
#################################

# print(Fruits)
# Fruits.remove("banana")
# print(Fruits)

# Fruits.append("banana")
# print(Fruits)
# Fruits.remove("banana")
# print(Fruits)

# print(Fruits)
# Fruits.pop(1)
# print(Fruits)

# print(Fruits)
# Fruits.pop()
# print(Fruits)

#################################
#         ### Loops ###         #
#################################

# for fruit in Fruits:
#     print(fruit)
    
# for i in range(len(Fruits)):
#     print(Fruits[i])

# i = 0
# while i < len(Fruits):
#     print(Fruits[i])
#     i += 1

#################################
#     ### Comprehension ###     #
#################################

Fruits = ["apple", "banana", "orange", "mango", "kiwi"]

# Way no. 1
# newlist = []

# for x in Fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# # Way no. 2
# newlist = [x for x in Fruits if "a" in x]

# print(newlist)

#################################
#        ### Copying ###        #
#################################

# Fruits2 = Fruits

# Fruits.pop()

# print(Fruits)
# print(Fruits2)

# Fruits3 = Fruits.copy()
# Fruits3 = Fruits[:]

# Fruits3 = [x for x in Fruits]

# Fruits3 = []
# for x in Fruits:
#     Fruits3.append(x)

# Fruits.pop()

# print(Fruits)
# print(Fruits3)
