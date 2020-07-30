#
# Example file for variables
#

# Declare a variable and initialize it

f=0
# print(f)

# # re-declaring the variable works

# f = "abc"
# print (f)

# ERROR: variables of different types cannot be combined
# remember this works in javascript, but not in python
#it does not work, the arguments have to agree with each other

#print("this is a string " + 123)


# it works this way lol

#print ("this is a string" + str(123))

# Global vs. local variabels in functions
def someFunction():
    f = "def"
    print(f)

someFunction()
print(f)

del f
print(f)






