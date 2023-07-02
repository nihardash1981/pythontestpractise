nom=int(input("enter how many multiplication table u want:"))
if (nom<=0):
    print("{} invalid input".format(nom))
else:
   for n in range(1,nom+1):
       print("-----------------------------------------")
       print("\tMul table for:{}".format(n))
       print("--------------------------------")
       for i in range(1,11):
           print("\t{} x {} ={}".format(n,i,n*i))
       else:
           print("-print all tables------------------")
       




            