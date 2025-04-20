#PROFIT AND LOSS CALCULATOR

#Used  variables to easily take input from user.
a=float(input("Enter current price of Share 1 : "))
p=float(input("Enter initial price of Share 1 bought: "))
q1=int(input("Enter Qty of Share1.: "))
b=float(input("Enter current prive of Share 2 : "))
q=float(input("Enter initial price of Share 2 bought: "))
q2=int(input("Enter Qty of Share 2.: "))

#Used operators to check the profit and loss
print(a*q1," is current total price of Share 1 shares.")
print(b*q2," is the current total price of Share 2 shares.")
x=(a*q1)-(p*q1)
y=(b*q2)-(q*q2)

#Nested if statements to print the profit and loss statements of each share.
if x>0:
    if y>0  :
        print(x," is Profit of Share 1 and ",y," is the Profit of Share 2 shares")
        print(x+y," is total PROFIT")
    else:
        print(x," is Profit of Share 1 and ",y," is the LOSS of Share 2 shares")
        print(x+y," is total PROFIT")
else:
    if y>0:
        print(x," is LOSS of Share 1 and ",y," is the Profit of Share 2 shares")
        print(x+y," is total PROFIT")
    else:
        print(x," is LOSS of Share 1 and ",y," is the LOSS of Share 2 shares")
        print(x+y," is total LOSS")