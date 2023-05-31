s1={10,20,30,"ram","rahim","pyhton",35.46}
print(s1)
fs1=frozenset(s1)
print(fs1,type(fs1)) ##class 'frozenset##
## print(fs1[0]) ##error frozenset' object is not subscriptable and u cant assign##
##fs1[0]=100 ##frozenset' object does not support item assignment##
lst=[10,20,30,40,10,"kvr","ram"]
print(lst,type(lst)) ##class 'list##
fs2=frozenset(lst)
print(fs2,type(fs2)) ##class 'frozenset no duplicate record##
tpl=(10,20,30,40,10,"kvr","ram",True)
print(tpl,type(tpl))
fs3=frozenset(tpl
print(fs3,type(fs3))) ##convert any type value into frozenset object##





