n=int(input("enter your number="))
sum=0
a=n
while a>0:
    d=a%10
    sum=sum+d**3
    a=a//10
if n==sum:
    print("AMSTRONG NUMBER")
else:
    print("NOT AN AMSTRONG NUMBER")