u=int(input("enter the units consumed="))
if u<50:
    c=u*2.60
    t=25
elif u<100:
    c=u*3.25
    t=35
elif u<200:
    c=u*5.26
    t=45
else:
    c=u*8.45
    t=75

total=c+t
print("the electricity bill is ",total)