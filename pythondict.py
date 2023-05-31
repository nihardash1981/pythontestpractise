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
d4.get(10)
print(d4)



