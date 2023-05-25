t1=(10,20,30,40,76,32,98)
print(t1,type(t1)) ###class tuple##
t2=(10,20,"kvr","naresh","python",32,9,12,7,True)
print(t2,type(t2)) ###class tuple accept both homogenous and hetrogenous data##
t3=()
print(t3,type(t3)) ###class tuple##
t3=tuple()
print(t3,type(t3)) ###class tuple###
t4=10,"travis","javis",67.98,76.98,"ouacet",2+3j
print(t4,type(t4)) ###class tuple without braces also tuple###
print(t4[0]) ###class tuple inndex value###
print(t4[-1]) ###class tuple index value
print(t4[::-1]) ###class tuple with slicing###
###convert list to tuple###
lst=[10,20,30,40,50,"python"]
print(lst,type(lst)) ###class
tpl=tuple(lst)
print(tpl,type(tpl)) ##class 'tuple convert list to tuple###
lst1=list(tpl)
print(lst1,type(lst1)) ###convert tuple to list###
t5=(10,20,30,40,50)
t5.count(10)
print(t5,type(t5))

