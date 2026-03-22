s=input("enter your string=")
c=input("enter the character you want to count=")
i=0
count=0
l=len(s)
print("the lenght of this string is",l)
while i<l:
    if s[i]==c:
        count=count+1
    i=i+1
print("the character appered",count,"times")