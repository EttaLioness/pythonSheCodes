#for loop
# my_iterable =  [1, 2, 3]

# for item in my_iterable:
#     #some code here
#     print(item)

# for num in range(10):
#     #every number default starts at 0, up to but not including the 
# last number listed
#     print(num)

# for num in range(5, 10):
#     #start from 5 up to but not including 
#     print(num)

# for num in range(5, 10, 2):
#     #start from 5 up to but not including 10 only every 2nd number
#     print(num)

# #type range-look type range up.
# type(range(1, 11))

#============================================================================
#EXERCISE
#Use a for loop to print numbers 0 to 100 (inclusive)
# for num in range(101):
#     print(num)

#Use a for loop to print the numbers 0 to 100 in steps of 5 (5, 10, 15, etc..)
# for num in range(0, 101, 5):
#     print(num)


chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
for item in range(len(chilli_wishlist)):
    print(chilli_wishlist[item])
    
for item in chilli_wishlist:
    print(item)

#==================================================================
#EXERCISE
#Adapt the for loop to print a message for each item in the list, e.g. “Chilli wants: item”.
# for item in range(len(chilli_wishlist)):
#     print(f"chilliwants {item}")
# #Use a for loop to print each item in a list from a previous exercise or example
# chilli_wishlist = [["igloo"],
# ["donut toy", "tennis ball", "crocodile toy"],
# ["chicken", "peanut butter"],
# ["cardboard box", "kong", "dig mat"]]

# for category in chilli_wishlists:
#     for item in category:
#         print(item)

#WHILE LOOPS
# some_boolean_condition = True
# while some_boolean_condition:
#     #do something
#     pass

# counter = 10
# while counter <=10:
#     print(counter)
#     counter = counter + 1 # equavalent to counter += 1 (cant do ++)#

#+++++++++++++++++++++++++++++++++++++++++++++
#NOTE CONTROL+C to stop infintite loop!!!!!!!!
+#+++++++++++++++++++++++++++++++++++++++++===

# guess = ""
# while guess != "a":
#     guess = input("Guess a letter: ")
