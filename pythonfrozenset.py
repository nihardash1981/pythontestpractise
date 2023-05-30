s1={10,20,30,"ram","rahim","pyhton",35.46}
print(s1)
fs1=frozenset(s1)
print(fs1,type(fs1)) ##class 'frozenset##
## print(fs1[0]) ##error frozenset' object is not subscriptable and u cant assign##
##fs1[0]=100 ##frozenset' object does not support item assignment##



