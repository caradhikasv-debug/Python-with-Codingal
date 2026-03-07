print("select you ride")
print("1. bike")
print("2. car")
c=input("enter your choice=")
if c=="1":
    print("select your bike")
    print("1. racing bike")
    print("2. dirt bike")
    c1=input("enter your choice=")
    if c1=="1":
        print("your racing bike is booked")
    else:
        print("your dirt bike is booked")

elif c=="2":
    print("select your car")
    print("1. sports car")
    print("2. SUV")
    c2=input("enter your choice=" )
    if c2=="1":
        print("your sports car is booked")
    else:
        print("your SUV is booked")
    
else:
    print("wrong choice")