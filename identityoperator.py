l1=[10,"abc",12.56]
l2=[10,"abc",12.56]
print (id(l1),id(l2))
print (l1 is l2) ##since menmory address are not same false
print (l2 is not l1)##since menmory address are not same true##
tpl1=(10,"abc")
tpl2=(10,"abc")
print(id(tpl1),id(tpl2))
print (tpl1 is tpl2)##since menmory address not same output as false
print (tpl1 is not tpl2)##since menmory address not same output as true##
s1={10,"python"}
s2={10,"python"}
print(id(s1),id(s2))
print (s1 is s2)##since menmory address is not same false
print (s2 is not s1)##since menmory address is same output as true##
s3=s1
print(id(s1),id(s3))
print(s1 is s3)
print(s1 is not s3)
##swallow copy in identifeier##
s4=s1.copy()
print(id(s1),id(s4))
print (s1 is s4)




