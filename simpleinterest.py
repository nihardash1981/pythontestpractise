p=float(input("enter principle amount"))
t=float(input("enter time:"))
r=float(input("enter rate of interst:"))
#cal si and amtpay
si=(p*t*r)/100
amtpay=p+si
#display the result##
print("."*50)
print("Result")
print("-"*50)
print("principal amount:",p)
print("time:",t)
print("rate of interst:",r)
print("simple interst in amount:",si)
print("total amount to pay=:",amtpay)
print("-"*50)