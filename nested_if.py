m=input("do you have a medical cause? Y/N=")
a=float(input("enter your attendance="))
if m=="Y":
    print("allow to sit in the exam")
else:
    if a>=75:
        print("allowed to sit in the exam")
    else:
        print("not allowed to sit in the exam")