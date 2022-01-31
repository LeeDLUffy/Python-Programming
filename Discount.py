#take purchase amount
#check amount and offer discount
#calculate net pay
amount=int(input("Enter amount:"))
discount=0.05*1000
Netpay=amount-discount
if(amount>=1000):
    print("Netpay:",Netpay)
else:
    print("No Discount Offered")