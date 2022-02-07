salary=float(input("Enter salary:"))
years=int(input("Enter years of service:"))
if (years>10):
    print("Net bonus amount:",(salary*0.1)+salary)
if (years>=6 and years<=10):
    print("Net bonus amount:",(salary*0.08)+salary)
if (years<6):
    print("Net bonus amount:",(salary*0.05)+salary)    