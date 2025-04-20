a=float(input("Enter current price of TCS Shares: "))
b=float(input("Enter current prive of Railtel Shares: "))
print(a*15," is current total price of TCS shares.")
print(b*20," is the current total price of Railtel shares.")
x=(a*15)-57474.75
y=(b*20)-8374
if x>0:
    if y>0  :
        print(x," is Profit of TCS and ",y," is the Profit of Railtel shares")
        print(x+y," is total PROFIT")
    else:
        print(x," is Profit of TCS and ",y," is the LOSS of Railtel shares")
        print(x+y," is total PROFIT")
else:
    if y>0:
        print(x," is LOSS of TCS and ",y," is the Profit of Railtel shares")
        print(x+y," is total PROFIT")
    else:
        print(x," is LOSS of TCS and ",y," is the LOSS of Railtel shares")
        print(x+y," is total LOSS")