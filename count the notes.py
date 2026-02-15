a=int(input("enter the amount="))
note1=a//100
note2=(a%100)//50
note3=((a%100)%50)//20

print("num of 100=",note1)
print("num of 50=",note2)
print("num of 20=",note3)