#we are practicing how to print a basic statement

#A double underscore prefix causes the Python interpreter to 
# rewrite the attribute name in order to avoid naming conflicts in subclasses. 
# This is also called name mangling—the interpreter changes the name of the variable in a way that makes 
# it harder to create collisions when the class is extended later.

def main ():
    print("Hello world")

if __name__ == "__main__":
    main()
    


