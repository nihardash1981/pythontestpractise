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
####################list remove function################
l1=[10,20,30,40,20,40,"donali","pyhton",30.40]
print(l1,type(l1))
l1.remove(20) ###first occurence of 20 will be removed########
print(l1,type(l1))
##########l1.remove(100) ####100 not in the list####  
######print(l1,type(l1)) ###output is value error####

###########list pop function########
l1=[10,20,30,40,20,50,10]
print(l1)
l1.pop(6)
print(l1,type(l1))
l1.pop(-2)
print(l1,type(l1))

########################pop function with index #########
l1=[10,"nihar","arbaz","python",12,2+1j]
print(l1)
l1.pop()###last index data will be removed########
print(l1)

#####clear function#######
l1=[10,"akash","pandit",2+3j,12]
l1.clear()
print(l1,len(l1))

#######delete function in list#######
l1=[10,20,30,40,50,90,60]
del(l1[1:3])
print(l1)
###count function in list#######
l1=[10,20,30,40,50,90,40,70]
print(l1.count(40))

###index function in list#######
l1=[10,20,10,20,40,30,40,50,90,10,40,70,30]
l1.index(40)
print(l1.index(40))

######swallow copy function in list,oject same but adress diffrent###
l1=[10,"python"]
print(l1,id(l1))
l2=l1.copy()
print(l2,id(l2))
l1.append("python")
l2.append("datasciences")
print(l1,id(l1))
print(l2,id(l2))
#############deep copy function in list#######
l1=[10,20,"python"]
print(l1,id(l1)) 
l2=l1 ###deepcopy with assignment operator
print(l2,id(l2))
l1.append("python")
print(l1,id(l1))
l2.append("dsc")
print(l2,id(l2))











      





