x=int(input("Enter the valof x: "))
y=int(input("Enter the valof y: "))
print("-"*50)
print("original value of x{}".format(x))
print("original value of y{}".format(y))
print("-"*50)
##swap the values logic##
x,y=y,x
print("swapped value of x{}".format(x))
print("swapped value of y{}".format(y))
print("-"*50)
##swap the values logic##
t=x
x=y
y=t
print("swapped value of x{}".format(x))
print("swapped value of y{}".format(y))
print("-"*50)

##swaping logic with XOR operator ##
x=x^y
y=x^y
print("swapped value of x{}".format(x))
print("swapped value of y{}".format(y))
print("-"*50)
