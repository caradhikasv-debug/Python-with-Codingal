a=int(input("enter value 1="))
b=int(input("enter value 2="))
c=int(input("enter value 3="))
avg=(a+b+c)/3
print(avg)
if avg>a and avg>b and avg>c:
    print("average is higher")
else:
    print("values are higher")