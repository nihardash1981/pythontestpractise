##write the python program to ** right angle pattern##
n=int(input("enter how many stars line u want:"))
if(n<=0):
    print ("{}invalid input".format(n))
else:
    for i in range(0,n):##inner for loop## i=3#       
        for j in range(0,i+1):##outer for loop iteration##j in range(0,4)
            print("*", end="")
            print()





