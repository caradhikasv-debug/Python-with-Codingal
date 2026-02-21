ac=float(input("enter the actual cost="))
sc=float(input("enter the sale cost="))
if sc>ac:
    amount=sc-ac
    print ("total profit=",amount)
else:
    print("no profit is made")