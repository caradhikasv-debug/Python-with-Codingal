def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("SIMPLE CALCULATOR")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

c=int(input("ENTER YOUR CHOICE(1-4) = "))
x=int(input("ENTER NUMBER 1 = "))
y=int(input("ENTER NUMBER 2 = "))

if c==1:
    print(x,"+",y,"=",add(x,y))
elif c==2:
    print(x,"-",y,"=",sub(x,y))
elif c==3:
    print(x,"*",y,"=",mul(x,y))
elif c==4:
    print(x,"/",y,"=",div(x,y))
else:
    print("invalid choice")
    