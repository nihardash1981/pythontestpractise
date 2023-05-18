l1=[10,20,30,40,50,60,70,80,90,100,-10,20]
print(l1,type(l1))
l2=[10,10.94, "rosan", "aguata",2+3j]
print(l2,type(l2))
l3=[]
print(l3,type(l3))
print(l2[1])
print(l2[-1])
print(l1[1:3]) #slicing the oobjects list
print(l1[1:-2])
print(l2,type(l2),id(l2))
l2[2]=23.89
print(l2,type(l2),id(l2)) #mutable list object

##############################list append function #################################
l1=[10,"ajanata"]
print(l1,type(l1),id(l1))
l1.append(10.98)
print(l1,type(l1),id(l1))
l1.append("python")
print(l1,type(l1),id(l1))
l2=[]
print(l2,type(l2),id(l2))
l2.append(190)
l2.append("python")
l2.append("donoli")
print(l2,type(l2),id(l2))
l3=list()
print(l3,type(l3),id(l3))
l3.append("true")
l3.append(2+4j)
l3.append("python")
print(l3,type(l3),id(l3))

###########condition with inner lists #####
l1=[10,20,30,40]
l2=[10,",ailesha"]
l2.append(l1)
print(l2,type(l2))

##############list insert function#################
l1=[10,"donali",30.40]
print(l1,type(l1))
l1.insert(2,"monoli")
print(l1,type(l1))
l1.insert(3,True)
print(l1,type(l1))

      





