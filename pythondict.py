a=10
print(a,type(a))
d={}
print(d,type(d))
##to find key and values in dict function##
d['st no']= 12
d['name']="rossum"
d['marks']=34.68
print(d,type(d))
d['cname']="OUCET"
print(d,type(d)) #class dict function##
d1={1:'python',2:'java',3:'DS',4:'AI',5:'JS'}
print(d1,type(d1)) #class 'dict' function##
d1[2]='Django' #update and change the value##
print(d1,type(d1))
del d1[2] ##delete the value##
print(d1,type(d1))
d2=dict()
print(d2,type(d2)) ##empty dict function##
##add value in empty dict function##
d2['stno']=123
d2['c12']="OUCET" ##string value single quote##
print(d2,type(d2)) #class dict function##
d2['place']="HYD"
print(d2,type(d2))

##non emmpty dict function##
d3={10:"Django",11:"AI"}
d3[10]="DS" #replace with django##
print(d3,type(d3))
d3[12]="Web Dev"##new entry##
print(d3,type(d3))

##function in dict##
##get Function##
d4={10:"OUCET",20:"JNTU(H)",30:"HCU",40:"KVR"}
print(d4,type(d4))
d4.get(10) ##output oucet##
print(d4,type(d4))
d4.get(20)
print(d4,type(d4))
d4.get(121)
print(d4,type(d4))
d4[10]
print(d4,type(d4))
##remove duplicates from list##
l1=[10,20,30,40,50,60,10,50]
s1=set(l1) ##convert into set and print
print(s1,type(s1))
##values in dict##
d1={10:"oucet",11:"jntu(h)",12:"hcu",13:"kvr"}
print(d1.values()) ##print list of values##
for x in d1.values():
    print(x,type(x))##print list of values##
##keys function in dict##
d1.keys()
for x in d1.keys():
    print(x,type(x))##print keys in dict##
##items function in dict #
# it returns both key and value##
d1.items()
print(d1.items()) ##output are key and values##
for x in d1.items():
    print(x,type(x))##print items in dict##
for k,v in d1.items():
    print(k,"-->",v)##print items in dict##

##pop function in dict##
##to remove key from dict##
d1.pop(11)
print(d1)
##popitem function in dict##
##to remove latest key and value from dict##
d1.popitem()
print(d1) ##remove latest item from dict##
##copy function in dict##
d2=d1.copy()
print(d2) ##copy function in dict##
d2[13]="kvr"
print(d2) ##copy of newly added  d2 data not reflect in d1t##
print(d1) ##copy function in dict##
d3={}
d3[15]="NU"
print(d3)
##to add d3 data in d2##
d3.update(d2)
print(d3)





         






