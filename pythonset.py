s1={10,20,30,40,50,10}
print(s1,type(s1)) ##class set###
s2={10,20,30,"kvr",10.33,True}
print(s2,type(s2)) ##class set###
s4=set()
print(s4,type(s4)) ##class set###
len=len(s1)
print(len,type(len)) ##class int###
s5={}
print(s5,type(s5)) ##class dict###
s1={10,20,30,40,50,10,19,23,43,98}
#print(s1[0]) ##TypeError:set object is not subscriptable indexing not feasible not maint insertion###
#print(s1[1:6]) ##TypeError:set object is not subscriptable slicing not feasible since not maintain insertion order###
s3={10,20,40,67,98,76,43}
print(s3,id(s3))##mutable object with addres {98, 67, 20, 40, 10, 43, 76} 2383119601888###
s3.add("hyd")
print(s3,type(s3),id(s1)) ##class
s4={10,"donoli"}
print(s4,type(s4),id(s4)) ##mutable object with add func  1937673311776###
s4.add("python")
s4.add(23.98)
print(s4,type(s4),id(s4)) ###mutable object with add func class set 1937673311776##
s5=set()
print(s5,type(s5),id(s5))##emplty set mutable  class set address 2696706283712####
s5.add("kvr")
s5.add("sds")
s5.add(100)
s5.add(200)
s5.add(100)
print(s5,type(s5),id(s5)) ##mutable and no duplicates allowed class set 2696706283712##

##clear function##
s6={10,"python","rossum",34.67,True} ##class 'set'> 2164787140576##
print(s6,type(s6),id(s6))
s6.clear()
print(s6,type(s6),id(s6)) ##class 'set'> 2164787140576##
##copy function in set###
s7={10,"python","rossum",2+3j,True}
print(s7,type(s7),id(s7)) ##class 'set'> 2721513953696 addres diffreent swallow copy##
s8=s7.copy()
print(s8,type(s8),id(s8)) ##class 'set'> 2721513953248 address diffreent swallow copy##
s7.add("java")
s8.add("django")
print(s7,type(s7),id(s7)) ##swallow copy function#
print(s8,type(s8),id(s8)) ##swallow copy function##

##deep copy function##
s9={10,"python","rossum",21.98}
print(s9,type(s9),id(s9)) ##
s10=s9
print(s10,type(s10),id(s10)) ##same mem space with same addres class 'set'> 1900706748832##
s9.add("Django")
##
t1=(10,"kvr",(10,20,30),"oucet")
print(t1)
l1=[10,"kvr",(10,20,30),"oucet"]
print(l1)
t1=(10,"kvr",[10,20,30],"oucet") ##inside the tuple we can take list also##
print(t1)
t2=(10,"kvr",{10,20,30},"oucet") ##inside the tuple we can take set also ##
print(t2)
l9=[10,"kvr",{10,20,30},"oucet"] ##inside the list we can take set also ##
print(l9)
##remove function python##
s11={10,"kvr","python",23.54,12}
print(s11)
s11.remove("python")
print(s11)
s11.remove("kvr")
print(s11)
## s11.remove(1000) ##KeyError ##

##discard function in set##
d1={10,"kvr","python",20,30}
print(d1)
d1.discard("python")
print(d1)
d1.discard("100")
print(d1) ###no error is coming##

###pop function in set##
p1={10,"kvr","python",20,21,32}
print(p1)
p1.pop()
print(p1)

###isdisjoint function in set##
isd1={10,20,30,40}
isd2={"apple","banana","orange","kiwi"}
isd3={10,20,60,87}
isd1.isdisjoint(isd2) ##TRUE is COMING NO COMMON ELEMENTS#
isd1.isdisjoint(isd3) ##false is COMING since  COMMON ELEMENTS##
##issuperset function in set##
iss1={10,20,30,40} ##iss called superset##
iss2={10,20} ##iss2 called subset##
iss3={10,20,50,60,55} ##iss3 called subset##
iss1.issuperset(iss2) 
print(iss1.issuperset(iss2)) ##true is coming in issuperset##
print(iss1.issuperset(iss3)) ##false is coming in issuperset not caontain all elements##

##issubset function in set##
sub1={10,20,30,40}
sub2={10,20}
sub3={10,20,50,60}
print(sub1.issubset(sub2)) ##false is coming all sub1 elements not present in sub2
print(sub1.issubset(sub3)) ##false is coming all sub1 elements not present in sub3
print(sub2.issubset(sub1)) ##true is coming all sub2 elements present in sub1

##union function inset##
u1={10,20,30,40}
u2={10,50,60,70}
u3=u1.union(u2)
print(u3)

##intersection function##
i1={10,20,30,40,50}
i2={10,50,40,70}
i3=i1.intersection(i2)
print(i3)

##bitwsie operator | ,& ,^, ##
cricket={"sachin","kohili","rohit"}
tennis={"rohit","ram","sindhu"} 
allplayers=cricket | tennis
print(allplayers) ##union oeration##
bothplayers=cricket & tennis
print(bothplayers) ##intersection oeration##
onlycricket=cricket-tennis
print(onlycricket)
onlytennis=tennis-cricket
print(onlytennis)
criten=tennis^cricket ##xor operator##
print(criten)



    

