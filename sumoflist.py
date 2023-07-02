##write a program sum of elements of the list##
lst=[10,20,45,30.56,12.45]
s=0
i=0
print ("-"*50)
print("elements of list:")
print("-"*50)
while(i<len(lst)):
    print("\t{}".format(lst[i]))
    s=s+lst[i]
    i=i+1
else:
    print("\tsum={}".format(s))


      