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
#############reverse  function in list#######
lst=[10,"python",23.44,"ara","hyderabad"]
lst.reverse()
print(lst,id(lst))
########### sort function in list#######
lst=[10,0,1,2,3,4,5,6,7,8,9,10,-23,-46,-48]
lst.sort()
print(lst) #print in ascending order##
lst=["apple","guava","jackfruit","orange","banana","stberry","mberry"]
lst.sort() #print
print(lst) #print in aescending order##
lst=[10,20,30,40,-45,-67,-1,-34]
lst.reverse() #reverse
print(lst) #print in descending order##
lst=[10,20,40,8,45,23,-12,-65,-54,-98,-12]
lst.sort(reverse=True) #sorting with reverse order##
print(lst)
lst=[10,13,12,98,67,23.76,98,-23,-45]
lst.sort(reverse=False) #sorting with reverse order##
print(lst) #print in ascending order##

##extend function in the list#####
lst1=["apple","guava","jackfruit","orange","banana"]
lst2=[12,45,98,90,43]
lst3=["bitroot","cinamonkey","chocolate","sand"]
lst1.extend(lst2) #extend function can take only one value in list##
lst1.extend(lst3) #extend function can take only one value##
print(lst1) #print

lst1=["apple","guava","jackfruit"]
lst2=[10,20,30,98,78,90]
lst3=[12,23,43,65,87]
lst1=lst1+lst2+lst3 #plus function also give the details like extend###
print(lst1)
#####inner list function in list##
lst=[11,"rossume",[10,20,30],[60,50,55],"apple"]
print(lst) #print
print(lst[0]) #first value of list
print(lst[2])
print(lst[2][1])
print(lst[2][1])
print(lst[2][-1])
print(lst[2][-2]) #
print(lst[-3][-2])
print(lst[-3][-3]) 
print(lst[-3][::-1])
print(lst[3])
print(lst[3].sort()) ##use sort function in list##
print(lst[4])
lst[2].append(14) #use append function in inner list###
print(lst[2])
lst[3].insert(2,25) #use insert function in inner list###
print(lst[3])
print(lst)
lst.pop(2) #remove inner list from list use pop ###
print(lst)
lst.pop(-2) #remove
print(lst) #remove inner list from list use pop by negative values##
l1=[18,16,19]
l2=[67,23,12]
lst.insert(2,l1) ##insert function added in list##
print(lst)
lst.append(l2)






     
     











      





